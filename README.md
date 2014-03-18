image-best-guess
================

Scraps Google image search results and finds best guess for the provided image. 

Console usage
-----

```bash
python image_best_guess.py image_url
```

Module usage
------------

```python
# Create ImageBestGuessFinder object
finder = ImageBestGuessFinder()
# Invoke find method
print(finder.find('http://media.tumblr.com/745c48c1dcf79c51f64f69c64d0cf095/tumblr_inline_ms5a0kJVT51qz4rgp.jpg')
```

Used libraries:
--------------

  * [Requests](http://docs.python-requests.org/en/latest/)
