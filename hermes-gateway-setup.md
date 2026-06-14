# Hermes Gateway Setup

## Files Created Outside This Repo

### ~/hermes-gateway-tmux.sh
Executable script that:
- Checks if tmux session "hermes" exists
- If not, creates it and starts "hermes gateway" inside
- If yes, attaches to it

### ~/Library/LaunchAgents/com.hermes-agent.gateway.plist
Launchd plist for Mac auto-start on login.

## To Enable Auto-Start
```bash
launchctl load ~/Library/LaunchAgents/com.hermes-agent.gateway.plist
```

## Notes
- tmux is NOT currently installed on this system
- Install with: `brew install tmux`
