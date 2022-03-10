#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

ExitWorld()
{
    send {Esc}+{Tab}{Enter}
    sleep, 100
    FileDelete, seed.txt
}

pyruner(){
    Run, powershell.exe
    sleep 1000
    Send python findSeed.py
    send {Enter}
    WinMinimize, Windows PowerShell
}

waitopen(){
    pyruner()
    MsgBox, Wait for 30 secs --Made by Mick4994
    sleep 30000
}

FSGOP(){
    SetKeyDelay, 0
    send {Esc}{Esc}{Esc}
    send {Tab}{Enter}
    SetKeyDelay, 45 ; Fine tune for your PC/comfort level
    send {Tab}
    SetKeyDelay, 0
    send {Tab}{Tab}{Enter}
    send ^a
    send ^v
    send {Tab}{Tab}{Enter}{Enter}{Enter}{Tab}{Tab}{Tab}
    SetKeyDelay, 45 ; Fine tune for your PC/comfort level
    send {Tab}{Enter}
    SetKeyDelay, 0
    send {Tab}{Tab}{Tab}^v{Shift}+{Tab}
    SetKeyDelay, 45 ; Fine tune for your PC/comfort level
    send {Shift}+{Tab}{Enter}
}

FSGtrue(){
    FileRead, seed, %A_WorkingDir%\seed.txt
    Clipboard= %seed%
    FSGOP()
}

FSGFastCreateWorld(){
    IfExist, seed.txt
        FSGtrue()
    IfNotExist, seed.txt
        ComObjCreate("SAPI.SpVoice").Speak("searching")
}

#IfWinActive, Minecraft
    {

        J::
            FSGFastCreateWorld()
        return

        U::
            ExitWorld()
        return

        ^!G::
            waitopen()
        return

    }