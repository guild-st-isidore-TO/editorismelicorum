\bookpart {
  \pointAndClickOff
  
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
        \new Voice = "TemplateLyricsLink" {
          \cadenzaOn \transpose c TemplateTransposeKey{ \stemUp \TemplateVocals }
        }
      >>
      \new Lyrics \lyricsto TemplateLyricsLink {
        \TemplateLyrics
      }
      \new Staff \with {
        instrumentName = "Guitar (accomp.)"
        shortInstrumentName = "Gtr-A"
      } {
        \clef "G_8"
        \TemplateGuitarAccomp
      }
      \new Staff \with {
        instrumentName = "Guitar (solo)"
        shortInstrumentName = "Gtr-S"
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