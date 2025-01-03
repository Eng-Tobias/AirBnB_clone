def test_update_state(self):
    """Tests that updating a state modifies its record in the table."""
    new_state = State(name="California")
    new_state.save()
    
    # Update the state
    new_state.name = "New California"
    new_state.save()
    
    # Check if the name was updated
    self.cursor.execute("SELECT name FROM states WHERE id = %s", (new_state.id,))
    updated_name = self.cursor.fetchone()[0]
    self.assertEqual(updated_name, "New California")
