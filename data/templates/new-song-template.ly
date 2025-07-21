\bookpart {
  \header {
    title = "TemplateTitle"
    subtitle = "TemplateSubtitle"
    instrument = "TemplateInstrument"
    composer = "TemplateComposer"
    arranger = "TemplateArranger"
  }

  \score{
    <<
      \new Staff <<
        \set Staff.midiInstrument = "flute"
        \set Staff.autoBeaming = ##f
        \new Voice = "TemplateLyricsLink" {
          \cadenzaOn \transpose c des{ \stemUp \TemplateMusic }
        }
      >>
      \new Lyrics \lyricsto TemplateLyricsLink {
        \TemplateLyrics
      }
      \new Staff {
        \clef "G_8"
        R1*20
      }
      \new Staff {
        \clef bass
        R1*20
      }
    >>
    \layout{
      \context {
        \Staff
        \override TimeSignature #'stencil = #point-stencil
        \override Slur #'stencil = ##f
      }
    }
    \midi{}
  }
}