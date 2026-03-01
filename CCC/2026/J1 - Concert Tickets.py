#Problem J1: Concert Tickets - 2026 (SirNooby)
besa_tickets = int(input())
total_tickets = int(input())
purchased_tickets = int(input())

remaining_tickets = total_tickets - purchased_tickets - besa_tickets

if (remaining_tickets) >= 0:
    print("Y", remaining_tickets)
else:
    print("N")