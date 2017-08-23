# service.streamlink.proxy

- Version: **3.0.5**
- Github: [neverreply/service.streamlink.proxy](https://github.com/neverreply/service.streamlink.proxy)
- Repo: [repository.neverreply](https://github.com/neverreply/repo)

## Custom streamlink plugins

- They can be used with [service.streamlink.plugins](https://github.com/neverreply/service.streamlink.plugins)

## IPTV Simple PVR
```
#EXTINF:-1 tvg-id="" tvg-shift="" tvg-name="" radio="" tvg-logo="example.png" group-title="English",Example
http://127.0.0.1:6539/?url=https://example.com/example&q=best
```
[neverreply/service.streamlink.proxy](https://github.com/neverreply/service.streamlink.proxy)
- `http://127.0.0.1:6539/?`
*will write the stream into the buffer*
- `http://127.0.0.1:6539/channel.m3u8?`
*will redirect the hls url instead of writing it into the buffer,
it does not work for every stream.*

VIDEO QUALITY
- `q=worst`
*if you want the **best** stream, you don't need to add this*

VIDEO URL
- `url=https://example.com/example`
or
- `url=https%3A%2F%2Fexample.com%2Fexample`

for the best solution the url should be encoded,
you can encode url's with an [urlencoder](https://www.urlencoder.org)

EXAMPLE
```
# before
https://www.youtube.com/watch?v=K59KKnIbIaM
# after
https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DK59KKnIbIaM
```
