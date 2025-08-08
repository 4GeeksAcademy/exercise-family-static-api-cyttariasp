"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Michael",
                "last_name": last_name,
                "age": 23,
                "lucky_numbers": [10, 23, 32]
            },
            {
                "id": self._generate_id(),
                "first_name": "Bobby",
                "last_name": last_name,
                "age": 43,
                "lucky_numbers": [17, 20, 29]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        

    def delete_member(self, id):
        for i, m in enumerate(self.members):
            if m["id"] == id:
                del self._members[i]
                return True
        return False
        

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
