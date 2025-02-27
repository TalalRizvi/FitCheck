import gui3d
import human
import os

def create_avatar(height, chest, waist, hips):
    # Access the currently selected human model
    human_obj = gui3d.app.selectedHuman

    # Ensure these modifier names match what you see in the MakeHuman interface
    try:
        # Set the height and other body dimensions
        human_obj.getModifier("measure/height").setValue(height / 100.0)  # Height in meters
        human_obj.getModifier("measure/chest circum").setValue(chest)
        human_obj.getModifier("measure/waist circum").setValue(waist)
        human_obj.getModifier("measure/hip circum").setValue(hips)

        # Export the avatar to an OBJ file
        export_path = os.path.join(os.path.expanduser("~"), 'Documents', 'makehuman', 'exports', 'avatar.obj')
        gui3d.app.doExport(export_path)

        print(f"Avatar exported to {export_path}")
    except Exception as e:
        print(f"Error setting modifiers: {e}")

# Test with sample measurements
height = 270  # in cm
chest = 100    # in cm
waist = 70    # in cm
hips = 95     # in cm
create_avatar(height, chest, waist, hips)
