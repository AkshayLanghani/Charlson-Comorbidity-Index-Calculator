import math
from typing import Dict, Tuple


class CharlsonComorbidityIndex:
    
    CONDITION_SCORES = {
        'age_under_50': 0,
        'age_50_59': 1,
        'age_60_69': 2,
        'age_70_79': 3,
        'age_80_plus': 4,
        'myocardial_infarction': 1,
        'chf': 1,
        'peripheral_vascular_disease': 1,
        'cva_tia': 1,
        'dementia': 1,
        'chronic_pulmonary_disease': 1,
        'connective_tissue_disease': 1,
        'peptic_ulcer_disease': 1,
        'liver_disease_mild': 1,
        'liver_disease_moderate_severe': 3,
        'diabetes_uncomplicated': 1,
        'diabetes_end_organ_damage': 2,
        'hemiplegia': 2,
        'moderate_severe_ckd': 2,
        'solid_tumor_localized': 2,
        'solid_tumor_metastatic': 6,
        'leukemia': 2,
        'lymphoma': 2,
        'aids': 6,
    }
    
    def __init__(self):
        self.selected_conditions = {}
        self.age = None
    
    def set_age(self, age: int) -> None:
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        
        self.age = age
    
    def add_condition(self, condition: str, present: bool = True) -> None:
        if condition not in self.CONDITION_SCORES:
            raise ValueError(f"Unknown condition: {condition}")
        
        self.selected_conditions[condition] = present
    
    def get_age_score(self) -> int:
        if self.age is None:
            raise ValueError("Age must be set before calculating score")
        
        if self.age < 50:
            return 0
        elif self.age < 60:
            return 1
        elif self.age < 70:
            return 2
        elif self.age < 80:
            return 3
        else:
            return 4
    
    def calculate_score(self) -> int:
        if self.age is None:
            raise ValueError("Age must be set before calculating score")
        
        total_score = self.get_age_score()
        for condition, present in self.selected_conditions.items():
            if present and not condition.startswith('age_'):
                total_score += self.CONDITION_SCORES[condition]
        
        return total_score
    
    def estimate_10_year_survival(self) -> float:
        score = self.calculate_score()
        
        survival_proportion = math.exp(-0.9 * score)
        survival_percentage = survival_proportion * 100
        
        return round(survival_percentage, 1)
    
    def get_results(self) -> Dict:
        score = self.calculate_score()
        survival = self.estimate_10_year_survival()
        
        return {
            'cci_score': score,
            '10_year_survival_percentage': survival,
            'age_score': self.get_age_score(),
            'selected_conditions': {
                k: v for k, v in self.selected_conditions.items() 
                if v and not k.startswith('age_')
            }
        }
    
    def reset(self) -> None:
        self.selected_conditions = {}
        self.age = None


def main():
    """Example usage of the Charlson Comorbidity Index calculator."""
    
    # Create calculator instance
    cci = CharlsonComorbidityIndex()
    
    print("=" * 60)
    print("EXAMPLE 1: 65-year-old with CHF and Diabetes")
    print("=" * 60)
    
    cci.set_age(65)
    cci.add_condition('chf', True)
    cci.add_condition('diabetes_uncomplicated', True)
    
    results = cci.get_results()
    print(f"Age: 65")
    print(f"Conditions: CHF, Uncomplicated Diabetes")
    print(f"CCI Score: {results['cci_score']}")
    print(f"Estimated 10-Year Survival: {results['10_year_survival_percentage']}%")
    
    # Example 2: 75-year-old with multiple conditions
    print("\n" + "=" * 60)
    print("EXAMPLE 2: 75-year-old with Multiple Conditions")
    print("=" * 60)
    
    cci.reset()
    cci.set_age(75)
    cci.add_condition('myocardial_infarction', True)
    cci.add_condition('chf', True)
    cci.add_condition('chronic_pulmonary_disease', True)
    cci.add_condition('moderate_severe_ckd', True)
    cci.add_condition('diabetes_end_organ_damage', True)
    
    results = cci.get_results()
    print(f"Age: 75")
    print(f"Conditions: MI, CHF, Chronic Pulmonary Disease, CKD, Diabetes with End-Organ Damage")
    print(f"CCI Score: {results['cci_score']}")
    print(f"Estimated 10-Year Survival: {results['10_year_survival_percentage']}%")
    
    # Example 3: 45-year-old with no conditions
    print("\n" + "=" * 60)
    print("EXAMPLE 3: 45-year-old with No Comorbidities")
    print("=" * 60)
    
    cci.reset()
    cci.set_age(45)
    
    results = cci.get_results()
    print(f"Age: 45")
    print(f"Conditions: None")
    print(f"CCI Score: {results['cci_score']}")
    print(f"Estimated 10-Year Survival: {results['10_year_survival_percentage']}%")


if __name__ == "__main__":
    main()
