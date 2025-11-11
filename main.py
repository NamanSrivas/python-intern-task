import requests

def fetch_and_display_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            users = response.json()
            
            if not users:
                print("No users found in the API response.")
                return
            
            print("=== ALL USERS ===\n")
            
            for index, user in enumerate(users, start=1):
                print(f"User {index}:")
                print(f"  Name: {user['name']}")
                print(f"  Username: {user['username']}")
                print(f"  Email: {user['email']}")
                print(f"  City: {user['address']['city']}")
                print("------------------------")

            # BONUS: Print only users whose city starts with 'S'
            
            print("\n=== USERS FROM CITIES STARTING WITH 'S' ===\n")
            s_city_users = [user for user in users if user['address']['city'].startswith('S')]
            
            if s_city_users:
                for index, user in enumerate(s_city_users, start=1):
                    print(f"User {index}:")
                    print(f"  Name: {user['name']}")
                    print(f"  Username: {user['username']}")
                    print(f"  Email: {user['email']}")
                    print(f"  City: {user['address']['city']}")
                    print("------------------------")
            else:
                print("No users found from cities starting with 'S'.")
        else:
            print(f"Error: API returned status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to API - {e}")

if __name__ == "__main__":
    fetch_and_display_users()
