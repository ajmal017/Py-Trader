import supertrend
import datetime
import print_supress
import argparse

if __name__ == '__main__':
    #TODO Implement last call through sessions
    #TODO Program reversals
    #TODO Send commands to running program
    
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", help="The symbol you want the bot to focus on")
    parser.add_argument("bias", help="Buying or selling bias")
    parser.add_argument("target", help="Target shares")
    args = parser.parse_args()
    
    symbol = args.symbol
    
    if args.bias == "buy":
        last_call = "SELL"
    else:
        last_call = "BUY"
    
    target = args.target
    t = supertrend.Bot(symbol)
    
    print(f"[{datetime.datetime.now()}]")
    print(f"Bot started with focus on {symbol}")
    
    #Main Loop
    while True:
        with print_supress.suppress_stdout_stderr():
            strat = t.strat(symbol)
        
        current_call = strat[0]
        
        if current_call == last_call:
            pass
        
        elif current_call == "BUY":
            last_call = current_call
            t.submit_order("BUY", target, strat[1])
            
            print(f"[{datetime.datetime.now()}]")
            print(f"New Call: Bought {target} shares of {symbol}")
            print(f"Set stop at {strat[1]}")
        
        elif current_call == "SELL":
            last_call = current_call
            t.submit_order("SELL", target, strat[1])
            
            print(f"[{datetime.datetime.now()}]")
            print(f"New Call: Sold {target} shares of {symbol}")
            print(f"Set stop at {strat[1]}")