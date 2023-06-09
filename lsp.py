import time
import pyautogui

# Time interval between cursor movements (default: 60 seconds)
interval = 60

pyautogui.FAILSAFE = False  # Disable fail-safe check

def move_cursor():
    while True:
        # Get the current position of the cursor
        original_position = pyautogui.position()

        # Move the cursor slightly in a random direction
        pyautogui.moveRel(1, 1)

        # Pause for a moment to allow the cursor movement to take effect
        time.sleep(0.1)

        # Get the new position of the cursor
        new_position = pyautogui.position()

        # Check if the new position is within the screen boundaries
        screen_width, screen_height = pyautogui.size()
        edge_margin = 1

        if new_position[0] <= edge_margin:  # Left edge
            dx = 1
            dy = 0
        elif new_position[0] >= screen_width - edge_margin:  # Right edge
            dx = -1
            dy = 0
        elif new_position[1] <= edge_margin:  # Top edge or corner
            dx = 0
            dy = 1
        elif new_position[1] >= screen_height - edge_margin:  # Bottom edge or corner
            dx = 0
            dy = -1
        else:
            # Cursor is not touching any edge or corner
            dx = 0
            dy = 0

        # Move the cursor away from the edge or corner
        pyautogui.moveRel(dx, dy)

        # Move the cursor back to the original position
        pyautogui.moveTo(original_position)

        # Pause before the next movement
        time.sleep(interval)

# Call the move_cursor function to start the cursor movement
move_cursor()
