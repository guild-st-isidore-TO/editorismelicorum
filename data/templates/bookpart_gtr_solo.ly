\bookpart {
  \pointAndClickOff

  \paper {
    left-margin = 0.8125\in
  }

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
        \set Staff.instrumentName = "Voice"
        \set Staff.shortInstrumentName = "Vox"
        \set Staff.midiInstrument = "flute"
        \set Staff.autoBeaming = ##f

        \clef "G_8"
        \new Voice = "TemplateLyricsLink" {
          \cadenzaOn \transpose c TemplateTransposeKey{ \stemUp \TemplateGuitarSolo }
        }
      >>
      \new Lyrics \lyricsto TemplateLyricsLink {
        \TemplateLyrics
      }
      \new Staff \with {
        instrumentName = "Gtr (solo)"
        shortInstrumentName = "Gt-S"
      } {
        \clef "G_8"
        \new Voice = "TemplateLyricsLink" {
          \cadenzaOn \transpose c TemplateTransposeKey{ \stemUp \TemplateGuitarSolo }
        }
      }
    >>
    \layout{
      \context {
        \Staff
        \override TimeSignature #'stencil = #point-stencil
        \override Slur #'stencil = ##f
      }
    }
  }
}