# track-matte

The "Track Matte Key" in Adobe Premiere applies a matte directly to an
underlying fill layer (i.e. video clip). It does so after mapping the
matte coordinates onto the coordinates of the underlying video clip 
(rather than the video *track*), so the matte and fill layer are stuck
together.  
    
While sometimes useful, this can be problematic if you would like to 
crop the spacial boundaries of a video clip *after* repositioning and 
resizing it (e.g. in the case of a video tiling, where many videos are 
shown simultaneously on the screen, each in its own separate boxed area).

The matte_rev_transform.py script lets you transform the fill layer
separately from the matte layer by calculating the appropriate values
that must be entered into the matte layer settings in Premiere to 
*reverse* this transformation.

Track mattes in action: https://youtu.be/PPQKYd4IDws

### e.g. Tiling layout:
![template]

### Videos positioned according to tiling layout:
![thumbnail]

[template]: https://raw.githubusercontent.com/chrismbryant/track-matte/master/Example%20Tiling%20Template/Give%20Us%20This%20Day%20(Tiling%20Template).jpg

[thumbnail]: https://raw.githubusercontent.com/chrismbryant/track-matte/master/Example%20Tiling%20Template/thumbnail_01.png
