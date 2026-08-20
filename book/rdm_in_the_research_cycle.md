# RDM in the Research Project Cycle

 ## What is Research Data Management? 
 :::{card} 
"Research Data Management (RDM) is a broad term that covers all aspects of handling research data throughout research, including planning, collecting, organising, documenting, storing, preserving, and sharing data. Effective RDM also covers the management of all resources involved in working with research data such as files, scripts [and tools]" (Li et al., 2025).  
::: 
<br>

## The Research Project Cycle

From start to finish, your thesis project will likely involve 5 key stages, as shown in this graphic for a typical research project cycle:  

<style>
/_static/Research_cycle_graphic.jpg{
  position: relative;
  width: 100%;
  max-width: 1400px;
  margin: 1.5rem auto;
}

/_static/Research_cycle_graphic.jpg{
  display: block;
  width: 100%;
  height: auto;
}

/* Invisible/visible hover targets */
.research-hotspot {
  position: absolute;
  width: 5.5%;
  aspect-ratio: 1;
  border-radius: 50%;
  cursor: help;
  outline: none;
}

/*
   The small circle becomes visible when the user
   hovers over or focuses a stage number.
*/
.research-hotspot::before {
  content: "";
  position: absolute;
  inset: 0;
  border: 3px solid rgba(0, 150, 160, 0.85);
  border-radius: 50%;
  background: rgba(0, 150, 160, 0.08);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.research-hotspot:hover::before,
.research-hotspot:focus::before {
  opacity: 1;
}

/* The tooltip */
.research-tooltip {
  position: absolute;
  z-index: 10;
  width: 330px;
  max-width: min(330px, 70vw);
  padding: 1rem 1.1rem;

  background: white;
  color: #333;

  border-radius: 10px;
  border: 1px solid rgba(0, 150, 160, 0.35);

  box-shadow:
    0 6px 20px rgba(0, 0, 0, 0.18);

  font-size: 0.92rem;
  line-height: 1.5;

  opacity: 0;
  visibility: hidden;
  pointer-events: none;

  transition:
    opacity 0.2s ease,
    transform 0.2s ease;

  transform: translateY(6px);
}

/* Tooltip heading */
.research-tooltip strong {
  display: block;
  margin-bottom: 0.45rem;

  font-size: 1rem;
  line-height: 1.3;
  color: #008f98;
}

/* Show tooltip on hover/focus */
.research-hotspot:hover .research-tooltip,
.research-hotspot:focus .research-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/*
   Positioning of the five numbered hotspots.

   These percentages are based on your 1400 × 1051 image.
*/

/* 1 — bottom left */
.stage-1 {
  left: 20.5%;
  top: 90.5%;
}

/* 2 — left middle */
.stage-2 {
  left: 3.0%;
  top: 48.5%;
}

/* 3 — upper left */
.stage-3 {
  left: 2.7%;
  top: 20.5%;
}

/* 4 — upper right */
.stage-4 {
  left: 62.5%;
  top: 20.5%;
}

/* 5 — lower right */
.stage-5 {
  left: 64.5%;
  top: 59.5%;
}


/*
   Tooltip positions.

   These are adjusted individually so that the boxes
   don't run off the edges of the image.
*/

.stage-1 .research-tooltip {
  bottom: 110%;
  left: -20px;
}

.stage-2 .research-tooltip {
  top: -20px;
  left: 120%;
}

.stage-3 .research-tooltip {
  top: -20px;
  left: 120%;
}

.stage-4 .research-tooltip {
  top: -20px;
  right: 120%;
}

.stage-5 .research-tooltip {
  top: -20px;
  right: 120%;
}


/* On smaller screens, make the tooltip a little smaller */
@media (max-width: 700px) {
  .research-tooltip {
    width: 260px;
    font-size: 0.85rem;
  }
}
</style>


<div class="research-cycle">

  <img
    src="_static/research_cycle.jpg"
    alt="Research data management cycle showing five stages from research ideas through data publishing, preservation and re-use."
  >


  <!-- =====================================================
       STAGE 1
       ===================================================== -->

  <div
    class="research-hotspot stage-1"
    tabindex="0"
    role="button"
    aria-label="Stage 1: Planning for Research Ideas"
  >
    <div class="research-tooltip">
      <strong>Stage 1 — Planning for Research Ideas</strong>

      Before you can plan how you'll manage your data, you first
      need to define what data you'll actually be working with.
      This stage helps you identify the research objects your
      project will involve, and flag early on whether any of that
      data carries ethical or legal considerations — since those
      can require significant lead time to sort out.
    </div>
  </div>


  <!-- =====================================================
       STAGE 2
       ===================================================== -->

  <div
    class="research-hotspot stage-2"
    tabindex="0"
    role="button"
    aria-label="Stage 2: Planning for Research Data and Design"
  >
    <div class="research-tooltip">
      <strong>Stage 2 — Planning for Research Data &amp; Design</strong>

      Once you know what data you're working with, the next
      decisions are where it will live and in what format.
      This stage covers the storage and file format choices that
      protect your data from loss and keep it usable by you and
      others down the line.
    </div>
  </div>


  <!-- =====================================================
       STAGE 3
       ===================================================== -->

  <div
    class="research-hotspot stage-3"
    tabindex="0"
    role="button"
    aria-label="Stage 3: Planning for Data Collection"
  >
    <div class="research-tooltip">
      <strong>Stage 3 — Planning for Data Collection</strong>

      With your data and storage plan in place, this stage turns
      to the collection process itself: describing your methods
      clearly, documenting your work as you go, and keeping files,
      folders, and code organised and traceable.
    </div>
  </div>


  <!-- =====================================================
       STAGE 4
       ===================================================== -->

  <div
    class="research-hotspot stage-4"
    tabindex="0"
    role="button"
    aria-label="Stage 4: Planning for Data Processing and Analysis"
  >
    <div class="research-tooltip">
      <strong>Stage 4 — Planning for Data Processing &amp; Analysis</strong>

      As data starts coming in, this stage is about protecting
      your raw data, keeping units and formats consistent, and
      maintaining a clear, reproducible link between your data,
      your analysis, and your results.
    </div>
  </div>


  <!-- =====================================================
       STAGE 5
       ===================================================== -->

  <div
    class="research-hotspot stage-5"
    tabindex="0"
    role="button"
    aria-label="Stage 5: Planning for Data Publishing, Preservation and Re-use"
  >
    <div class="research-tooltip">
      <strong>Stage 5 — Planning for Data Publishing, Preservation &amp; Re-use</strong>

      As your project wraps up, this final stage covers what
      happens to your data next: what should be shared, archived,
      or deleted, how to document it for others, where it should
      live long-term, and how it should be licensed.
    </div>
  </div>

</div>










<center>
<img src="graphics/Research_cycle_graphic_edited.jpg" alt="Research Project Cycle in 5 steps" style="width: 600px; height: auto;"/>
<p style="font-size: x-small;"><em>Adapted from "Project Cycle" by Scriberia, The Turing Way Community, licensed under CC-BY-4.0.</em></p>
</center>


A **data management plan** maps out in advance what you intend to do with research data during each part of the project cycle. This mini-module will guide you through key questions and considerations for managing research data effectively at each stage of the research process. 
<br>

## Download this checklist! 

Before you continue on in the mini-module, download this RDM checklist: 
:::{card} 
[**Download the Checklist**](graphics/Checklist_v1.docx).
:::
The checklist is meant to accompany the mini-module so that you can apply the guiding questions to plan your own project. We suggest that you download and/or print it out, jot notes in the margins, and bring it to planning discussions with your thesis supervisor. 

## Why plan for RDM? 

Let's illustrate why planning for research data management is essential by looking at four examples of researchers who did not effectively manage the data for their projects:  

::::{card-carousel} 2
:::{card} Scenario 1: No backups  
Emma spent months collecting data for her thesis on marine biodiversity [around off-shore wind farms]. Hundreds of hours went into snorkeling trips, labeling samples, and inputting data into Excel. She kept everything on her laptop. One rainy evening, her laptop wouldn’t turn on. No backup. No cloud sync. Just the sound of her academic dreams slowly drowning. 
:::
:::{card}  Scenario 2: Missing documentation 
Carlos did everything right, or so he thought. He conducted experiments, organized his folders, and saved everything on the university network. But when his advisor asked for the specific settings used for the analysis, such as the settings on the mass spectrometer he used to identify the peptides from [a collection of biological samples], Carlos realized he hadn’t documented anything. Worse, he couldn’t remember if he used the same setup for all experiments.   
:::
:::{card}  Scenario 3: Redundant file naming  
Alina had over 20 versions of [the] final dataset [for her thesis project], each slightly different. She named them things like Final.csv, FinalReal.csv, Final_FIXED.csv, And USE_THIS_ONE_final2.csv. 

During a meeting, her supervisor questioned her statistical analysis. Alina tried to trace it back but couldn’t figure out which dataset she [had used to write her final report].  
:::
:::{card} Scenario 4: Late ethics application 
For his master's thesis, Michel plans to look at people's experiences in a flight simulator. He will collect data on each participant's heart rate and temperature before and during the simulation. He will also ask participants to fill out a survey after their experiences in the simulator. Michel mistakenly thinks that his project doesn't involve personal data. But he is, indeed, planning to collect personal data that can be traced back to individual people. This requires ethical approval from TU Delft's Human Research Ethics Committee (the HREC)! 

Michel has taken time to recruit participants, booked precious time in the simulator, and gotten the software all set up. But he then learns that HREC must approve his research *before* he can proceed with data collection. He rushed to complete the HREC application materials, then has to wait several weeks for the committee's decision. This causes delays in data collection. Michel isn't sure if he'll get his project finished in time. 
:::
::::
<p style="font-size: x-small;"><em>Scenarios #1-3 re-used and adapted from: Li, M., Marcoux, K., Nazareth, D., Nikuze, A., & Plomp, W. (2025, December). Research Data Management Guidebook for Students. Zenodo. <a href="https://doi.org/10.5281/zenodo.15576176" target="_blank"> https://doi.org/10.5281/zenodo.15576176</a></em></p>
<br>

## Benefits of RDM 
In this mini-module we hope to reinforce the knowledge and skills that are required to prevent research setbacks like the four scenarios just described. As these examples demonstrate, there are good reasons to develop a strong data management plan and to internalize habits of planning for research data management. The benefits for you include:   

- **increased efficiency** by mapping how you will organise, document and store the data for your project (kind of like getting all your ingredients and tools out before you start to cook something).  

- **avoiding complications and delays** that stem from issues like data loss, inconsistent documentation, redundant file naming, and missing approvals.  

- making your **research methods more transparent**, making it easier for others to **re-use or reproduce** and verify your findings.  

- making your research more **FAIR** (Findable, Accessible, Interoperable and Reusable). In other words, it makes your research reproducible by others (including yourself!). Published research that adheres to FAIR principles is cited more and has a higher impact score (Alves, 2024). 

- developing **project planning and management skills** that will benefit you in academia or the workforce.  

- **saving you time and reducing stress** during your thesis project, especially at the end when good RDM will make it easier to write your report: by getting organised at the beginning of your project, you will save time at the end. 
<br>

## The Research Project Cycle: Check your understanding

Check your understanding of key ideas for RDM in the Research Project Cycle by answering these quiz questions: 
```{h5p} https://tudelft.h5p.com/content/1292947760806373647
```
<br> 
