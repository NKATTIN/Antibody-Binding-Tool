from pydantic import BaseModel

class OpticalDensityData(BaseModel):
    index: int
    optical_density: float
    amino_acid_sequence: str

class Statistics(BaseModel):
    amino_acid_sequence: str
    min: float
    max: float
    mean: float