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
          \cadenzaOn \transpose c des{ \TemplateMusic }
        }
      >>
      \new Lyrics \lyricsto TemplateLyricsLink {
        \TemplateLyrics
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