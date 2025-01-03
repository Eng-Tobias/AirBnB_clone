def test_delete_state(self):
    """Tests that deleting a state removes its record from the table."""
    new_state = State(name="Texas")
    new_state.save()

    # Get the state ID and delete it
    state_id = new_state.id
    new_state.delete()

    # Verify the state is deleted
    self.cursor.execute(
        "SELECT COUNT(*) FROM states WHERE id = %s", (state_id,)
    )
    count = self.cursor.fetchone()[0]
    self.assertEqual(count, 0)
