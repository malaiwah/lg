[![Docker Stars](https://img.shields.io/docker/stars/malaiwah/lg.svg)](https://hub.docker.com/r/malaiwah/lg/) [![Docker Pulls](https://img.shields.io/docker/pulls/malaiwah/lg.svg)](https://hub.docker.com/r/malaiwah/lg/)
# Looking Glass
[![](https://images.microbadger.com/badges/version/malaiwah/lg.svg)](https://microbadger.com/images/malaiwah/lg "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/malaiwah/lg.svg)](https://microbadger.com/images/malaiwah/lg "Get your own image badge on microbadger.com")

This is a simple, not-very-cleverly-named looking glass tool. Supports pinging and MTRing arbitrary addresses. Also supports dns lookup, nping (tcp-ping on port 80) and iperf3 client.

## Docker Image
Simply running `sudo docker run -d -p 8080:8080 malaiwah/lg` will get you a container running this app under http on port 8080, in an rbash environment restricted to only running `ping` and `mtr`.
You can also expose port 5201 (`-p 5201:5201`) to allow connections to the iPerf3 daemon.
