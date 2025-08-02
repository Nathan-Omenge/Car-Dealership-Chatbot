
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionSearchVehicles(Action):
    def name(self) -> Text:
        return "action_search_vehicles"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get entities from user message
        make = tracker.get_slot("make")
        fuel_type = tracker.get_slot("fuel_type") 
        price_range = tracker.get_slot("price_range")
        
        # Basic response (expand with actual database search)
        if make:
            message = f"I found several {make} vehicles in our inventory."
        else:
            message = "Let me search our inventory for you."
            
        dispatcher.utter_message(text=message)
        return []
