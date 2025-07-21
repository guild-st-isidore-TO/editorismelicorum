%{
  GregoBase metadata:
  - name
  - office-part
  - mode
  - book
  - transcriber

  Document header:
  - title: name
  - subtitle: office-part
  - instrument: mode
  - composer: book
  - arranger: transcriber
  - poet: ...
  - meter: ...
  - piece: ...
%}

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
      \new Voice = "theme" {
        \cadenzaOn \transpose c des{ \TemplateThemeName }
      }
    >>
    \new Lyrics \lyricsto theme {
      \TemplateThemeLyrics
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