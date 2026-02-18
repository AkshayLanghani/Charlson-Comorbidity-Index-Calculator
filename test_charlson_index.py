import unittest
from charlson_index import CharlsonComorbidityIndex


class TestCharlsonComorbidityIndex(unittest.TestCase):
    """Test cases for CCI calculator."""
    
    def setUp(self):
        self.cci = CharlsonComorbidityIndex()

    def test_age_under_50(self):
        self.cci.set_age(45)
        self.assertEqual(self.cci.get_age_score(), 0)
    
    def test_age_50_59(self):

        self.cci.set_age(55)
        self.assertEqual(self.cci.get_age_score(), 1)
    
    def test_age_60_69(self):

        self.cci.set_age(65)
        self.assertEqual(self.cci.get_age_score(), 2)
    
    def test_age_70_79(self):

        self.cci.set_age(75)
        self.assertEqual(self.cci.get_age_score(), 3)
    
    def test_age_80_plus(self):
        self.cci.set_age(85)
        self.assertEqual(self.cci.get_age_score(), 4)
    
    def test_age_boundary_50(self):
        self.cci.set_age(50)
        self.assertEqual(self.cci.get_age_score(), 1)
    
    def test_age_boundary_60(self):
        self.cci.set_age(60)
        self.assertEqual(self.cci.get_age_score(), 2)
    
    def test_age_boundary_80(self):
        self.cci.set_age(80)
        self.assertEqual(self.cci.get_age_score(), 4)
    
    def test_invalid_age_negative(self):
        with self.assertRaises(ValueError):
            self.cci.set_age(-5)
    
    def test_invalid_age_too_high(self):
        with self.assertRaises(ValueError):
            self.cci.set_age(200)

    def test_single_1point_condition(self):

        self.cci.set_age(45)
        self.cci.add_condition('myocardial_infarction', True)
        self.assertEqual(self.cci.calculate_score(), 1)
    
    def test_multiple_1point_conditions(self):

        self.cci.set_age(45)
        self.cci.add_condition('myocardial_infarction', True)
        self.cci.add_condition('chf', True)
        self.cci.add_condition('dementia', True)
        self.assertEqual(self.cci.calculate_score(), 3)
    
    def test_2point_conditions(self):

        self.cci.set_age(45)
        self.cci.add_condition('hemiplegia', True)
        self.assertEqual(self.cci.calculate_score(), 2)
    
    def test_3point_condition(self):

        self.cci.set_age(45)
        self.cci.add_condition('liver_disease_moderate_severe', True)
        self.assertEqual(self.cci.calculate_score(), 3)
    
    def test_6point_conditions(self):

        self.cci.set_age(45)
        self.cci.add_condition('solid_tumor_metastatic', True)
        self.assertEqual(self.cci.calculate_score(), 6)
        
        self.cci.reset()
        self.cci.set_age(45)
        self.cci.add_condition('aids', True)
        self.assertEqual(self.cci.calculate_score(), 6)
    
    def test_condition_removal(self):
        """Setting condition to False should remove points."""
        self.cci.set_age(45)
        self.cci.add_condition('chf', True)
        self.assertEqual(self.cci.calculate_score(), 1)
        
        self.cci.add_condition('chf', False)
        self.assertEqual(self.cci.calculate_score(), 0)
    
    def test_invalid_condition(self):
        with self.assertRaises(ValueError):
            self.cci.add_condition('invalid_condition', True)
    
    # ============================================================================
    # Combined Scoring Tests
    # ============================================================================
    
    def test_age_and_conditions_combined(self):
        """Age and condition scores should accumulate."""
        self.cci.set_age(65)  # 2 points
        self.cci.add_condition('myocardial_infarction', True)  # 1 point
        self.cci.add_condition('chf', True)  # 1 point
        self.assertEqual(self.cci.calculate_score(), 4)
    
    def test_complex_patient_example(self):
        """
        Test: 75-year-old with:
        - Age 75 = 3 points
        - MI = 1 point
        - CHF = 1 point
        - Chronic pulmonary disease = 1 point
        - CKD = 2 points
        - Diabetes with end-organ damage = 2 points
        Total = 10 points
        """
        self.cci.set_age(75)
        self.cci.add_condition('myocardial_infarction', True)
        self.cci.add_condition('chf', True)
        self.cci.add_condition('chronic_pulmonary_disease', True)
        self.cci.add_condition('moderate_severe_ckd', True)
        self.cci.add_condition('diabetes_end_organ_damage', True)
        
        self.assertEqual(self.cci.calculate_score(), 10)
    
    def test_no_conditions_minimal_age(self):
        """Healthy young patient should have score 0."""
        self.cci.set_age(25)
        self.assertEqual(self.cci.calculate_score(), 0)
    
    def test_no_conditions_age_50(self):
        """50-year-old with no conditions should have score 1."""
        self.cci.set_age(50)
        self.assertEqual(self.cci.calculate_score(), 1)
    
    # ============================================================================
    # Survival Estimation Tests
    # ============================================================================
    
    def test_score_0_survival(self):
        """Score 0 should give 100% survival."""
        self.cci.set_age(25)
        survival = self.cci.estimate_10_year_survival()
        self.assertAlmostEqual(survival, 100.0, places=1)
    
    def test_score_5_survival(self):
        """Score 5 should give ~1.1% survival."""
        self.cci.set_age(25)
        self.cci.add_condition('myocardial_infarction', True)
        self.cci.add_condition('chf', True)
        self.cci.add_condition('dementia', True)
        self.cci.add_condition('hemiplegia', True)  # 2 points
        
        survival = self.cci.estimate_10_year_survival()
        # e^(-0.9 * 5) * 100 ≈ 1.1%
        self.assertAlmostEqual(survival, 1.1, places=0)
    
    def test_survival_decreases_with_score(self):
        """Higher scores should give lower survival."""
        self.cci.set_age(25)
        survival_low = self.cci.estimate_10_year_survival()
        
        self.cci.add_condition('aids', True)
        survival_high = self.cci.estimate_10_year_survival()
        
        self.assertGreater(survival_low, survival_high)
    
    def test_high_score_survival_near_zero(self):
        """Very high scores should give near-zero survival."""
        self.cci.set_age(85)  # 4 points
        # Add multiple high-value conditions
        self.cci.add_condition('solid_tumor_metastatic', True)  # 6 points
        self.cci.add_condition('aids', True)  # 6 points
        self.cci.add_condition('diabetes_end_organ_damage', True)  # 2 points
        self.cci.add_condition('moderate_severe_ckd', True)  # 2 points
        
        survival = self.cci.estimate_10_year_survival()
        self.assertLess(survival, 0.1)
    
    # ============================================================================
    # Results Dictionary Tests
    # ============================================================================
    
    def test_get_results_structure(self):
        """get_results() should return expected dictionary structure."""
        self.cci.set_age(65)
        self.cci.add_condition('chf', True)
        
        results = self.cci.get_results()
        
        self.assertIn('cci_score', results)
        self.assertIn('10_year_survival_percentage', results)
        self.assertIn('age_score', results)
        self.assertIn('selected_conditions', results)
    
    def test_get_results_values(self):
        """get_results() values should match calculated values."""
        self.cci.set_age(65)
        self.cci.add_condition('chf', True)
        
        results = self.cci.get_results()
        
        self.assertEqual(results['cci_score'], 3)
        self.assertEqual(results['age_score'], 2)
        self.assertEqual(results['10_year_survival_percentage'], 
                        self.cci.estimate_10_year_survival())
    
    def test_get_results_excludes_false_conditions(self):
        """selected_conditions should only include True conditions."""
        self.cci.set_age(65)
        self.cci.add_condition('chf', True)
        self.cci.add_condition('dementia', False)
        
        results = self.cci.get_results()
        
        self.assertIn('chf', results['selected_conditions'])
        self.assertNotIn('dementia', results['selected_conditions'])
    
    # ============================================================================
    # Reset Functionality Tests
    # ============================================================================
    
    def test_reset_clears_age(self):
        """reset() should clear age."""
        self.cci.set_age(65)
        self.cci.reset()
        
        # Age should now be None
        with self.assertRaises(ValueError):
            self.cci.calculate_score()
    
    def test_reset_clears_conditions(self):
        """reset() should clear all conditions."""
        self.cci.set_age(65)
        self.cci.add_condition('chf', True)
        self.assertEqual(self.cci.calculate_score(), 3)
        
        self.cci.reset()
        # Should raise error because age is cleared
        with self.assertRaises(ValueError):
            self.cci.calculate_score()
    
    def test_reset_allows_new_patient(self):
        """After reset(), should be able to enter new patient data."""
        self.cci.set_age(65)
        self.cci.add_condition('chf', True)
        self.cci.reset()
        
        self.cci.set_age(45)
        self.cci.add_condition('dementia', True)
        
        self.assertEqual(self.cci.calculate_score(), 1)
    
    # ============================================================================
    # Edge Cases
    # ============================================================================
    
    def test_all_conditions_true(self):
        """Adding all conditions should give maximum score."""
        self.cci.set_age(85)  # 4 points
        
        all_conditions = [
            'myocardial_infarction',
            'chf',
            'peripheral_vascular_disease',
            'cva_tia',
            'dementia',
            'chronic_pulmonary_disease',
            'connective_tissue_disease',
            'peptic_ulcer_disease',
            'liver_disease_mild',
            'diabetes_uncomplicated',
            'hemiplegia',
            'moderate_severe_ckd',
            'solid_tumor_localized',
            'leukemia',
            'lymphoma',
        ]
        
        for condition in all_conditions:
            self.cci.add_condition(condition, True)
        
        score = self.cci.calculate_score()
        # Should be significantly high
        self.assertGreater(score, 20)
    
    def test_diabetes_choice_uncomplicated(self):
        """Only uncomplicated diabetes should be counted."""
        self.cci.set_age(45)
        self.cci.add_condition('diabetes_uncomplicated', True)
        self.cci.add_condition('diabetes_end_organ_damage', False)
        
        # Should only count uncomplicated (1 point)
        self.assertEqual(self.cci.calculate_score(), 1)
    
    def test_diabetes_choice_end_organ(self):
        """Only end-organ damage diabetes should be counted."""
        self.cci.set_age(45)
        self.cci.add_condition('diabetes_uncomplicated', False)
        self.cci.add_condition('diabetes_end_organ_damage', True)
        
        # Should only count end-organ damage (2 points)
        self.assertEqual(self.cci.calculate_score(), 2)
    
    def test_liver_disease_choice_mild(self):
        """Only mild liver disease should be counted."""
        self.cci.set_age(45)
        self.cci.add_condition('liver_disease_mild', True)
        self.cci.add_condition('liver_disease_moderate_severe', False)
        
        self.assertEqual(self.cci.calculate_score(), 1)
    
    def test_liver_disease_choice_severe(self):
        """Only severe liver disease should be counted."""
        self.cci.set_age(45)
        self.cci.add_condition('liver_disease_mild', False)
        self.cci.add_condition('liver_disease_moderate_severe', True)
        
        self.assertEqual(self.cci.calculate_score(), 3)


class TestMDCalcAlignment(unittest.TestCase):
    """Verify calculator matches MDCalc output for known examples."""
    
    def test_mdcalc_example_1(self):
        """MDCalc example: Healthy 45-year-old."""
        cci = CharlsonComorbidityIndex()
        cci.set_age(45)
        
        self.assertEqual(cci.calculate_score(), 0)
        self.assertAlmostEqual(cci.estimate_10_year_survival(), 100.0, places=0)
    
    def test_mdcalc_example_2(self):
        """MDCalc example: 65-year-old with CHF and Diabetes."""
        cci = CharlsonComorbidityIndex()
        cci.set_age(65)
        cci.add_condition('chf', True)
        cci.add_condition('diabetes_uncomplicated', True)
        
        # Age: 2, CHF: 1, Diabetes: 1 = 4
        self.assertEqual(cci.calculate_score(), 4)
        # Should match MDCalc's ~2-3% survival
        survival = cci.estimate_10_year_survival()
        self.assertGreater(survival, 1)
        self.assertLess(survival, 5)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
