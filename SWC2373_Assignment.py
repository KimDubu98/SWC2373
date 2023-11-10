import requests

webex_token = input("Enter your Webex token number: ")

base_url = "https://api.ciscospark.com/v1/"

# Option 0
def test_connection():
    url = base_url + "people/me"
    headers = {"Authorization": f"Bearer {webex_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Connection with Webex server is successful.")
    else:
        print("Connection test failed.")

# Option 1
def get_user_info():
    url = base_url + "people/me"
    headers = {"Authorization": f"Bearer {webex_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print("User Information: ")
        print("Display Name : ", user_info["displayName"])
        print("Nickname : ", user_info["nickName"])
        print("Email : ", user_info["emails"])
    else:
        print("Failed to get user information.")

# Option 2
def list_rooms():
    url = base_url + "rooms"
    headers = {"Authorization": f"Bearer {webex_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rooms = response.json()["items"]
        print("List of Rooms : ")
        for room in rooms:
            print("Room ID : ", room["id"])
            print("Room Title : ", room["title"])
            print("Date Created : ", room["created"])
            print("Last Activity : ", room["lastActivity"])
    else:
        print("Failed to fetch room list.")

# Option 3
def create_room():
    room_title = input("Enter the title of the room : ")
    url = base_url + "rooms"
    headers = {"Authorization": f"Bearer {webex_token}"}
    data = {"title": room_title}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Room created successfully.")
    else:
        print("Failed to create a room.")

# Option 4
def send_message():
    list_rooms()
    room_id = input("Enter the Room ID to send a message to: ")
    message = input("Enter the message: ")
    url = base_url + f"messages"
    headers = {"Authorization": f"Bearer {webex_token}"}
    data = {"roomId": room_id, "text": message}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send the message.")

# Main menu
while True:
    print("\nMain Menu:")
    print("0. Test Connection with Webex Server")
    print("1. Display User Information")
    print("2. List of Rooms")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Exit")
    
    choice = input("Enter your choice (0-5): ")
    
    if choice == "0":
        test_connection()
    elif choice == "1":
        get_user_info()
    elif choice == "2":
        list_rooms()
    elif choice == "3":
        create_room()
    elif choice == "4":
        send_message()
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (0-5).")
