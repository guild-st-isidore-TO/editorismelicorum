
\version "2.24.4"

#(set-default-paper-size "letter")

\include "../build/ly/ed_meli_example_vars.ly"

\book {

  %%------------------------------------
  %% Header & Paper Configurations

  \include "./parts/editoris_melicorum_header.ly"
  \include "./parts/editoris_melicorum_paper.ly"

  %%------------------------------------
  %% Title Page

  \include "../build/ly/ed_meli_example_title.ly"
  
  %%------------------------------------
  %% Table of Contents, Preface

  \include "./parts/editoris_melicorum_toc_preface.ly"


  %%------------------------------------
  %% Main Content

  \include "../build/ly/ed_meli_example_bookparts.ly"
}
