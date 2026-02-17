from datetime import datetime

# Conference Configuration
EVENT_INFO = {
    "name": "Google Cloud Summit 2026",
    "date": "October 15, 2026",
    "location": "Moscone Center, San Francisco, CA",
    "description": "Join us for a day of innovation, learning, and connection as we explore the future of cloud technology.",
    "schedule_start": "09:00",
    "lunch_start": "12:00",
    "lunch_duration_minutes": 60
}

# Talks Data
TALKS = [
    {
        "id": 1,
        "title": "Keynote: The Future of Cloud AI",
        "category": "AI/ML",
        "time": "09:00 - 10:00",
        "description": "Opening remarks on the latest advancements in Generative AI and Google Cloud's vision for the future.",
        "speakers": [
            {
                "first_name": "Sundar",
                "last_name": "Pichai (Clone)",
                "linkedin": "https://www.linkedin.com/in/sundarpichai/"
            }
        ]
    },
    {
        "id": 2,
        "title": "Serverless Architectures at Scale",
        "category": "Infrastructure",
        "time": "10:15 - 11:00",
        "description": "Learn how to build resilient, auto-scaling applications using Cloud Run and Cloud Functions.",
        "speakers": [
            {
                "first_name": "Sarah",
                "last_name": "Connor",
                "linkedin": "https://www.linkedin.com/in/sarahconnor-dummy"
            },
            {
                "first_name": "Kyle",
                "last_name": "Reese",
                "linkedin": "https://www.linkedin.com/in/kylereese-dummy"
            }
        ]
    },
    {
        "id": 3,
        "title": "BigQuery: Analyzing Petabytes in Seconds",
        "category": "Data Analytics",
        "time": "11:15 - 12:00",
        "description": "Deep dive into BigQuery optimization techniques and new features for real-time analytics.",
        "speakers": [
            {
                "first_name": "Data",
                "last_name": "Commander",
                "linkedin": "https://www.linkedin.com/in/datacommander-dummy"
            }
        ]
    },
    # Lunch 12:00 - 13:00 (Handled in logic/template)
    {
        "id": 4,
        "title": "Kubernetes for the Rest of Us",
        "category": "Infrastructure",
        "time": "13:00 - 13:45",
        "description": "Simplifying GKE management and security best practices for everyday developers.",
        "speakers": [
            {
                "first_name": "Alice",
                "last_name": "Kubernetes",
                "linkedin": "https://www.linkedin.com/in/alicek8s-dummy"
            }
        ]
    },
    {
        "id": 5,
        "title": "Vertex AI: From Prototype to Production",
        "category": "AI/ML",
        "time": "14:00 - 14:45",
        "description": "A hands-on walkthrough of deploying custom ML models using Vertex AI pipelines.",
        "speakers": [
            {
                "first_name": "Bob",
                "last_name": "Builder",
                "linkedin": "https://www.linkedin.com/in/bobbuilder-dummy"
            },
            {
                "first_name": "Wendy",
                "last_name": "Worker",
                "linkedin": "https://www.linkedin.com/in/wendyworker-dummy"
            }
        ]
    },
    {
        "id": 6,
        "title": "Security in the Cloud Era",
        "category": "Security",
        "time": "15:00 - 15:45",
        "description": "Zero Trust principles and how to implement them effectively in your GCP environment.",
        "speakers": [
            {
                "first_name": "Sec",
                "last_name": "Officer",
                "linkedin": "https://www.linkedin.com/in/secofficer-dummy"
            }
        ]
    },
    {
        "id": 7,
        "title": "Networking Deep Dive",
        "category": "Networking",
        "time": "16:00 - 16:45",
        "description": "Understanding VPCs, Load Balancing, and Hybrid Connectivity options.",
        "speakers": [
            {
                "first_name": "Net",
                "last_name": "Worker",
                "linkedin": "https://www.linkedin.com/in/networker-dummy"
            }
        ]
    },
    {
        "id": 8,
        "title": "Closing Keynote: Building for Tomorrow",
        "category": "General",
        "time": "17:00 - 17:45",
        "description": "Wrap up of the day and a look ahead at what's coming next in the Google Cloud ecosystem.",
        "speakers": [
            {
                "first_name": "Thomas",
                "last_name": "Kurian (Clone)",
                "linkedin": "https://www.linkedin.com/in/thomaskurian/"
            }
        ]
    }
]
