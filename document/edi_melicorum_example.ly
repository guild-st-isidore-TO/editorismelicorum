
\version "2.24.4"

#(set-default-paper-size "letter")

\include "../build/ly/ed_meli_example_vars.ly"

\book {
  %% book paper, which is inherited by all children bookparts
  \paper {
    ragged-last-bottom = ##t
    %% Page footer: add a different part-tagline at part last page
    oddFooterMarkup = \markup {
      \column {
        \fill-line {
          %% Copyright header field only on book first page.
          \if \on-first-page \fromproperty #'header:copyright
        }
        \fill-line {
          %% Part tagline header field only on each part last page.
          \if \on-last-page-of-part \fromproperty #'header:parttagline
        }
        \fill-line {
          %% Tagline header field only on book last page.
          \if \on-last-page \fromproperty #'header:tagline
        }
      }
    }

    % There's a bug in Times New Roman font shipped by Apple. Gotta change it.
    % see https://stackoverflow.com/questions/79562896/why-would-lilypond-be-replacing-capital-n-in-lyrics-with-u1eca-latin-capital-l
    property-defaults.fonts.serif = "Garamond"
    % property-defaults.fonts.sans = "DejaVu Sans"
    % property-defaults.fonts.typewriter = "Courier New"

    left-margin = 0.625\in
    bottom-margin = 0.625\in
    right-margin = 0.625\in
    top-margin = 0.625\in

    tocItemMarkup = \tocItemWithDotsMarkup
  }

  %% book header, which is inherited by the first bookpart
  \header {
    copyright = "FABRICA SALVADORIS MMXXV (Copyright - Salvador Workshop, 2025)"
    parttagline = "gen. by Editoris Melicorum"
    tagline = "Example Songbook [DRAFT]"
  }

  \bookpart {
    %% a different page breaking function may be used on each part
    \paper { page-breaking = #ly:minimal-breaking }

    \header {
      title =  \markup \center-column { 
        \vspace #2
        "EDITORIS MELICORUM"
        "Example Guitar Songbook"
      }
      subtitle = \markup \center-column { 
        \vspace #1
        "FABRICA SALVADORIS MMXXV" 
        \italic "Salvador Workshop, 2025"
      }
      subsubtitle = \markup \center-column { 
        \vspace #1
        "Faciebat Torontinum (Canada)"
        \typewriter "versio nulla.vii"
      }
    }

    \markup \vspace #2
    \markup \wordwrap {
      This songbook example has some Gregorian-style hymns (in Standard Notation) with space for
      writing arrangements. This file was generated through \bold "Editoris Melicorum"
      \italic "(Publishers of Music/Melodies)", a software project by
      \italic "Salvador Workshop" and the \italic "Society of St. Isidore (TO)"
    }

    \markup \vspace #1
    \markup \wordwrap {
      This project aims to create a digital music typesetting toolkit for use by music ministries
      in Catholic parishes. Its main objectives are building musical accompaniments around
      traditional hymns (the kind written in Gregorian notation), and laying them out into
      documents for use by the community.
    }

    \markup \vspace #1
    \markup \wordwrap {
      As initial steps, the Editoris project is building some proofs of concept:
      songbooks with traditional style accompaniments written out for classical guitar.
      And the sheets to enable musicians to create those arrangements.
    }

    \markup \vspace #1
    \markup \wordwrap {
      Please note that this is a work in progress, and there might be some buggy things
      that should be fixed promptly.
    }

    \markup \vspace #1
    \markup \wordwrap {
      For more info, the code repository is at \bold https://github.com/soc-st-isidore-TO/editorismelicorum
    }

    \pageBreak

    \markup \vspace #1
    \markuplist \table-of-contents

    \markup \vspace #2
    \markup \wordwrap {
      The music was sourced from GregoBase (https://gregobase.selapa.net/scores.php) and
      converted by the Editoris into modern standard notation.
    }

    \markup \vspace #1
    \markup \wordwrap {
      There are two staves below each hymn. The guitar part is written in Treble clef,
      octave below. And under that is a general/keyboard part in Bass clef, actual pitch.
    }

    \markup \vspace #1
    \markup \wordwrap {
      Note that when writing for guitar, the lowest pitch on standard notation is E2, or 
      on the first ledger line below the Bass clef. Extended range guitars can reach to
      B1, or under the second ledger line below the Bass clef.  Some guitars with
      longer scale lengths can go even lower to A1.
    }

    \markup \vspace #1
    \markup \wordwrap {
      Source documents have been abbreviated as follows:
    }

    \markup \vspace #1
    \markup \left-column {
      \line { \bold "L.Ant '60" "--- Liber antiphonarius, 1960" }
      \line { \bold "L.Usu '61" "--- The Liber Usualis, 1961" }
      \line { \bold "Ch.otC '56" "--- Chants of the Church, 1956" }
      \line { \bold "G.Rom '08" "--- Graduale Romanum, 1908" }
      \line { \bold "G.Rom '61" "--- Graduale Romanum, 1961" }
      \line { \bold "G.Rom '74" "--- Graduale Romanum, 1974" }
      \line { \bold "G.Smp '75" "--- Graduale simplex, 1975" }
      \line { \bold "Gr.Mis '90" "--- Gregorian Missal, 1990" }
      \line { \bold "L.Cant '83" "--- Liber cantualis, 1983" }
    }

    \markup \vspace #1
    \markup \wordwrap {
      Other abbreviations:
    }

    \markup \vspace #1
    \markup \left-column {
      \line { \bold "lib. info." "--- librarium informaticum" \italic "(database)" }
      \line { \bold "descr." "--- describébat" \italic "(transcribed in/by)" }
    }
  }
  

  \include "../build/ly/ed_meli_example_bookparts.ly"
}
