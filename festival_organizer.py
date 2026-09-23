# Festival Organizer
# A 3x3 matrix: Rows represent time slots
# Columns represent stages (Stage 1, Stage 2, Stage 3)
# Format per slot: [Band Name, Time, Votes]

festival_board = []

def setup_festival():
    print("="*45)
    print("FESTIVAL SETUP")
    print("="*45)
    print("Let's build the schedule! You will need 3 time slots and 3 bands per slot.\n")
    
    for i in range(3):
        time_slot = input(f"Enter the time for Slot {i+1} (e.g., 18:00): ").strip()
        current_row = []
        
        for j in range(3):
            band_name = input(f"  -> Enter the band name for Stage {j+1} at {time_slot}: ").strip()
            current_row.append([band_name, time_slot, 0])
            
        festival_board.append(current_row)
        print("-" * 30)
        
    print("Festival schedule built successfully!\n")

def print_voting_menu():
    print("\n--- BAND SCHEDULE & VOTING IDs ---")
    print(f"{'ID':<4} | {'Band':<20} | {'Time':<5} | {'Votes'}")
    print("-" * 45)
    
    id_counter = 1
    for i in range(3):
        for j in range(3):
            band = festival_board[i][j][0]
            time_slot = festival_board[i][j][1]
            votes = festival_board[i][j][2]
            print(f"[{id_counter}] | {band:<20} | {time_slot:<5} | {votes}")
            id_counter += 1
            
        print("-" * 45)

def validate_vote(position, voted_rows):
    mapping = {
        "1": (0,0), "2": (0,1), "3": (0,2),
        "4": (1,0), "5": (1,1), "6": (1,2),
        "7": (2,0), "8": (2,1), "9": (2,2)
    }

    if position not in mapping:
        print("INVALID INPUT: You must type a number between 1 and 9. Try again.")
        return False

    row, col = mapping[position]
    
    if row in voted_rows:
        time_slot = festival_board[row][col][1]
        print(f"COLLISION: You already picked a band for the {time_slot} slot. Pick a different time.")
        return False
        
    else:
        festival_board[row][col][2] += 1
        voted_rows.append(row) 
        print(f"--> Vote registered for {festival_board[row][col][0]} at {festival_board[row][col][1]}!")
        return True

def verify_final_schedule():
    print("\n" + "="*50)
    print("FINAL FESTIVAL ITINERARY")
    print("="*50)
    
    conflicts = [] 
    
    for i in range(3):
        time_slot = festival_board[i][0][1]
        max_votes = max(band[2] for band in festival_board[i])
        
        if max_votes == 0:
            print(f"At {time_slot} -> No votes. Time to get food!")
        else:
            tied_bands = [band for band in festival_board[i] if band[2] == max_votes]
            
            if len(tied_bands) == 1:
                print(f"At {time_slot} -> Go see {tied_bands[0][0]} ({max_votes} votes)")
            else:
                band_names = " and ".join([band[0] for band in tied_bands])
                print(f"At {time_slot} -> TIE DETECTED! ({max_votes} votes each)")
                conflicts.append((time_slot, band_names))
    
    if conflicts:
        print("\n" + "!"*50)
        print("WARNING: SCHEDULE CONFLICTS DETECTED")
        print("The group is divided! You must discuss and resolve:")
        for time_slot, bands in conflicts:
            print(f" - At {time_slot}: Tie between {bands}")
        print("!"*50)

def festival_app():
    setup_festival()
    
    running_votes = True
    
    while running_votes:
        # Reset votes to 0 at the start of every new round
        for i in range(3):
            for j in range(3):
                festival_board[i][j][2] = 0

        # Ask for the number of friends for this specific round
        while True:
            try:
                total_friends = int(input("\nHow many friends are voting in this round? "))
                if total_friends > 0:
                    break
                else:
                    print("You need at least 1 friend to play!")
            except ValueError:
                print("INVALID INPUT: Please enter a whole number.")

        current_friend = 1
        keep_voting = True

        while keep_voting:
            print("\n" + "="*45)
            print(f"TURN FOR FRIEND {current_friend}")
            print("ATTENTION: You have 3 votes. You must pick ONE band per time slot.")
            print("="*45)
            
            print_voting_menu()
            
            votes_cast = 0
            voted_rows = [] 
            
            while votes_cast < 3:
                position = input(f"Enter the ID (1-9) of the band you vote for ({votes_cast + 1}/3): ").strip()
                
                if validate_vote(position, voted_rows):
                    votes_cast += 1

            current_friend += 1

            if current_friend > total_friends:
                keep_voting = False
                print("\nAll friends have voted! Calculating the best schedule...")

        verify_final_schedule()
        
        # Ask if they want to run another voting session
        while True:
            another_vote = input("\nIs there going to be another vote? (yes/no): ").strip().lower()
            if another_vote in ['yes', 'y']:
                print("\nRestarting voting process. Clearing previous votes...")
                break
            elif another_vote in ['no', 'n']:
                running_votes = False
                print("\nThanks for using the Festival Organizer! Have fun at the concerts!")
                break
            else:
                print("INVALID INPUT: Please type 'yes' or 'no'.")

# Run the app
festival_app()
