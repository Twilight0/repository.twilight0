To use it in your subtitle addon first you have make it depend on script.module.sublib. 
Then you have to write your own service in total composed from 2 methods as show in below simple example.

```python
    import sublib
    import os

    class mysubtitlesite(sublib.service):

        def search(self):
            print self.item
            sub = self.sub("Test Subtitle", "en")
            sub.download("http://a.com/b/c.srt")
            self.addsub(sub)

        def download(self, link)
            fname = os.path.join(self.path, "test.srt")
            with open(fname, "w") as f:
                f.write(self.download(link))
            self.addfile(fname)
```

to see it in action simply initialize your class in the module that your "lib" attribute points in your addon.xml

```python
	import myservice
	
	myservice.mysubtitlesite()
```  

Thats all.