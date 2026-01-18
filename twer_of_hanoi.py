#Solved Using recursion
def tower_of_hanoi(n, source, helper, destination):
    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to helper
    tower_of_hanoi(n - 1, source, destination, helper)

    # Step 2: Move the largest disk to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move n-1 disks from helper to destination
    tower_of_hanoi(n - 1, helper, source, destination)


# ---- Driver Code ----
n = int(input("Enter number of disks: "))
tower_of_hanoi(n, "A", "B", "C")

