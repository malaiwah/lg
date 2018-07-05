# Looking Glass

This is a simple, not-very-cleverly-named looking glass tool. Supports pinging and MTRing arbitrary addresses.

## Docker Image
Simply running `sudo docker run -d malaiwah/lg` will get you a container running this app under http on port 8080, in an rbash environment restricted to only running `ping` and `mtr`.

## Caveats

I don't do any rate-limiting.
