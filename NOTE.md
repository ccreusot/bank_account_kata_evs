# Event TransactionRequest Emitted by xxxx

Valide transaction : 
    Account -> TransactionRequest (+10) -> EventDispatcher -> Bank -> Validate -> EventDispatcher -> Operation(+10) -> BalanceManager -> Account

# What do what

EventDispatcher
    - dispatch some transaction
        - for Request type, add transaction to event dispatcher, then ask Bank if it's possible
        - for accepted/rejected, informe balance manager of update

Bank
    - check some transaction
        - ask BalanceManager status of some account
        - Accept all positive Transaction
        - Decline negative Transaction when the new balance < -100, otherwise accept
        - dispatch event (accepted/rejected) through EventDispatcher
        
BalanceManager
    - compute balance for some account
    - on update, save transaction (only accepted onces)


