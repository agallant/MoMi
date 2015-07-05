#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       momi2midi.py
#      
#       Copyright 2015 www.soycode.com
#      
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU Lesser General Public License as published
#       by the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#      
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#      
#       You should have received a copy of the GNU Lesser General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import midi


class Track:
  """Represents a monophonic MIDI track."""
  def __init__(self, bpm=120):
    self.pattern = midi.Pattern()  # MIDI pattern (contains a list of tracks)
    self.track = midi.Track()  # MIDI track (contains list of MIDI events)
    self.pattern.append(self.track)
    tempo = midi.SetTempoEvent(tick=0)
    tempo.set_bpm(bpm)
    self.track.append(tempo)

  def add_note(self):
    # Instantiate a MIDI note on event, append it to the track
    on = midi.NoteOnEvent(tick=0, velocity=10, pitch=midi.G_3)
    self.track.append(on)
    # Instantiate a MIDI note off event, append it to the track
    off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
    self.track.append(off)

  def render(self):
    # Add the end of track event, append it to the track
    eot = midi.EndOfTrackEvent(tick=1)
    self.track.append(eot)
    # Print out the pattern
    print self.pattern
    # Save the pattern to disk
    midi.write_midifile("example.mid", self.pattern)


def main():
  track = Track()
  track.add_note()
  track.render()


if __name__ == "__main__":
  main()
