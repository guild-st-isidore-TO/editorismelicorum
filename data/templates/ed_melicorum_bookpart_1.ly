\bookpart {
  \header {
    title = "TemplateTitle"
    subtitle = \markup \italic { "TemplateSubtitle - TemplateInstrument" }
    composer = "TemplateComposer"
    arranger = "TemplateArranger"
    meter = "lib. info: TemplateDatabase"
  }

  \tocItem \markup { \bold "TemplateTitle" — \italic "TemplateSubtitle, TemplateInstrument" }
  \score{
    <<
      \new Staff <<
        \set Staff.midiInstrument = "flute"
        \set Staff.autoBeaming = ##f
        \new Voice = "TemplateLyricsLink" {
          \cadenzaOn \transpose c TemplateTransposeKey{ \stemUp \TemplateMusic }
        }
      >>
      \new Lyrics \lyricsto TemplateLyricsLink {
        \TemplateLyrics
      }
      \new Staff {
        \clef "G_8"
        R1*60
      }
      \new Staff {
        \clef bass
        R1*60
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