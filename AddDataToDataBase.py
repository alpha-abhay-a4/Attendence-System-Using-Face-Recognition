import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' :"https://faceattendancesystem-2e26e-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={

    "Roll no-25":
        {
            "Name": "Samrat Madake",
            "id": "D-25",
            "Branch": "CS(DS)",
            "starting_year": 2023,
            "total_attendance":5,
            #"standing":"6",
            "year":1,
            "last_attendance_time":"2024-02-19 00:9:40"

        },
    "Roll no-39":
        {
            "Name": "Abhay Patil",
            "id": "D-39",
            "Branch": "CS",
            "starting_year": 2023,
            "total_attendance": 5,
           # "standing": "6",
            "year": 1,
            "last_attendance_time": "2024-02-19 00:9:20"

        },
    "Roll no-54":
        {
            "Name": "Nirajan Pawar",
            "id": "D-54",
            "Branch": "CS",
            "starting_year": 2023,
            "total_attendance": 5,
           # "standing": "6",
            "year": 1,
            "last_attendance_time": "2024-02-19 00:9:35"

        },
}

for key,value in data.items():
    ref.child
