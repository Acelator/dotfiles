import XMonad

import XMonad.Hooks.ManageDocks
import XMonad.Hooks.SetWMName

-- Utilities
import XMonad.Util.Run

main :: IO ()
main = do
    spawnPipe("xmobar $HOME/.config/xmobar/.xmobarrc &")
    spawnPipe("picom")
    xmonad $ docks $ def
     {
       modMask                  = myModMask,
       terminal                 = myTerminal,
       borderWidth              = myBorderWidth,
       workspaces               = myWorkspaces,
       normalBorderColor        = myNormColor,

       startupHook = setWMName "LG3D",
       focusedBorderColor       = myFocusColor
     } --Separate config


myTerminal :: String
myTerminal = "alacritty"

myModMask :: KeyMask
myModMask = mod4Mask            --super

myBorderWidth :: Dimension
myBorderWidth = 2

myFocusColor :: String
myFocusColor = "#ff0000"

myNormColor :: String
myNormColor = "#6a83ab"


myWorkspaces = ["main","dev","www","4","5","6","7","8","9"]