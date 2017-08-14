def matte_calc(res = [1920, 1080], s0 = 100):

    '''
    This function calculates the X, Y, and Scale values which reverse a 
    transformation applied to a track matte in Adobe Premiere.

        The "Track Matte Key" in Adobe Premiere applies a matte directly to an
        underlying fill layer (i.e. video clip). It does so after mapping the
        matte coordinates onto the coordinates of the underlying video clip 
        (rather than the video *track*), so the matte and fill layer are stuck
        together.  
    
        While sometimes useful, this can be problematic if you would like to 
        crop the spacial boundaries of a video clip *after* repositioning and 
        resizing it (e.g. in the case of a video tiling, where many videos are 
        shown simultaneously on the screen, each in its own separate boxed area).

    In short, when a fill layer is transformed, the matte transforms with 
    it. This function will calculate and print the values required for input
    into the matte clip settings to reverse the transformation.

    VARIABLES:
    res - video resolution [width, height] (default: [1920, 1080]) 
    s0 - initial scale percentage value (default: 100)

    '''
    x0 = res[0]/2 # default X position value
    y0 = res[1]/2 # default Y position value

    print("\n----------------Clip Settings-----------------\n")

    x1 = float(input("    Video X Pos: "))
    y1 = float(input("    Video Y Pos: "))
    s1 = float(input("    Video Scale: "))

    k = s1/s0
    dx = x1 - x0
    dy = y1 - y0

    s2 = s0/k
    x2 = x0 - dx/k
    y2 = y0 - dy/k

    print("\n----------------Matte Settings----------------\n")
    print("    Tile X pos: " + str(x2))
    print("    Tile Y pos: " + str(y2))
    print("    Tile Scale: " + str(s2))

    again = input("\n    Calculate again? (Quit = q): ")
    
    if again.lower() == "q":
        exit()
    else:
        tile_calc()

def main():
    print("\n**********************************************")
    print("  Welcome! Enter your clip settings and I")
    print("  will return the matte settings you require.")
    print("**********************************************")
    matte_calc()
    
if __name__ == '__main__':
  main()
