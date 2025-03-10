class UserProfileManager:
    def __init__(self):
        self.user_profiles = {
            1: "Alice's Profile",
            2: "Bob's Profile",
            3: "Charlie's Profile"
        }

    def fetch_user_profile(self, user_id):
        """Retrieve the user profile for the given user ID."""
        return self.user_profiles.get(user_id, "Profile not found")

    def modify_user_profile(self, user_id, new_profile):
        """Modify the user profile for the given user ID."""
        self.user_profiles[user_id] = new_profile

    def handle_user_request(self, requested_user_id, update_user_id):
        """Handle a user request by fetching and modifying profiles."""
        profile = self.fetch_user_profile(requested_user_id)
        print(f"Fetched Profile for User ID {requested_user_id}: {profile}")

        self.modify_user_profile(update_user_id, f"Updated Profile for User ID {update_user_id}")
        print(f"Updated Profile for User ID {update_user_id}")

if __name__ == "__main__":
    manager = UserProfileManager()

    requested_user_id = 2
    update_user_id = 3

    manager.handle_user_request(requested_user_id, update_user_id)
