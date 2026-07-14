from pydantic import BaseModel
from typing import List

class BasicDetails(BaseModel):
    full_name: str
    nationality: str
    current_role: str
    industry: str
    current_city_country: str

class Profile(BaseModel):
    executive_summary: str
    basic_details: BasicDetails
    biography: str
    career_timeline: List[str]
    education: List[str]
    interests: List[str]
    estimated_net_worth: str
    recent_news: List[str]
    references: List[str]