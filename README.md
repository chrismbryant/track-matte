# track-matte

The "Track Matte Key" in Adobe Premiere maps a matte to a video clip
(rather than a video *track*). This is problematic if, for instance,
you'd like to crop the spacial boundaries of a video clip after 
repositioning and resizing it so that it can be used in a video 
tiling (i.e. where many videos are shown simultaneously on the screen, 
each in its own separate boxed area). In short, when you transform the 
video clip, the matte transforms with it.

The matte_rev_transform.py script lets you transform the fill layer
separately from the matte layer by calculating the appropriate values
to enter into the matte layer settings in Premiere.
