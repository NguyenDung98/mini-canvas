# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def events_api(request):
    return Response([
  {
    "id": "evt-001",
    "timestamp": "2023-10-27T10:00:00Z",
    "location": {
      "latitude": 34.0522,
      "longitude": -118.2437
    },
    "severity": "high",
    "description": "Unidentified vessel detected off the coast of Los Angeles."
  },
  {
    "id": "evt-002",
    "timestamp": "2023-10-27T11:30:00Z",
    "location": {
      "latitude": 40.7128,
      "longitude": -74.0060
    },
    "severity": "medium",
    "description": "Anomalous communication signal intercepted near New York City."
  },
  {
    "id": "evt-003",
    "timestamp": "2023-10-27T12:15:00Z",
    "location": {
      "latitude": 48.8566,
      "longitude": 2.3522
    },
    "severity": "low",
    "description": "Routine satellite pass over Paris confirms normal activity."
  },
  {
    "id": "evt-004",
    "timestamp": "2023-10-27T14:00:00Z",
    "location": {
      "latitude": 35.6895,
      "longitude": 139.6917
    },
    "severity": "high",
    "description": "Cybersecurity breach detected in Tokyo financial district."
  }
])
