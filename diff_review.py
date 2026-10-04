import subprocess
import sys
import os

def get_staged_diff():
    """Gets the diff of staged changes in Git."""
    try:
        # Use 'git diff --cached' to get the diff of staged changes
        result = subprocess.run(['git', 'diff', '--cached'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting staged diff: {e}", file=sys.stderr)
        print("Make sure you are in a Git repository and have staged changes.", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: 'git' command not found. Make sure Git is installed and in your PATH.", file=sys.stderr)
        return None

def review_diff(diff_content):
    """Simulates a basic review process for the diff content."""
    if not diff_content:
        print("No staged changes to review.")
        return

    print("--- Local Code Review (Pre-Push) ---")
    print("Reviewing staged changes...")
    print("\n" + diff_content)

    # In a real tool, this would involve more sophisticated analysis
    # or sending to a colleague. Here, we just print it.
    print("\n--- Review Complete ---")
    print("Consider these changes before pushing.")

def main():
    """Main function to orchestrate the diff review process."""
    # Check if we are in a Git repository
    if not os.path.exists('.git'):
        print("Error: Not in a Git repository.", file=sys.stderr)
        sys.exit(1)

    staged_diff = get_staged_diff()
    review_diff(staged_diff)

if __name__ == "__main__":
    main()
