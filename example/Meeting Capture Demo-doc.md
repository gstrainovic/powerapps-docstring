
Power App Documentation
=======================

Contents
========

* [Meeting Capture Demo](#meeting-capture-demo)
	* [OnStart](#onstart)
* [Connections](#connections)
* [Screens](#screens)
	* [2201_2](#2201_2)
	* [WelcomeScreen](#welcomescreen)
	* [HomeScreen](#homescreen)
	* [Sketch Screen](#sketch-screen)
	* [CameraScreen](#camerascreen)
	* [EmailScreen](#emailscreen)
	* [AttachmentsScreen](#attachmentsscreen)
	* [ConfirmScreen](#confirmscreen)
	* [ExportScreen](#exportscreen)
	* [FollowUpScreen](#followupscreen)
	* [FollowUpTimesScreen](#followuptimesscreen)
	* [HomePopUpsScreen](#homepopupsscreen)
	* [ExportPopUpsScreen](#exportpopupsscreen)
	* [CollectionsAndVariables](#collectionsandvariables)
	* [TestEmptyScreen](#testemptyscreen)
* [Global Variables](#global-variables)
	* [ShowMeetingTimes](#showmeetingtimes)
	* [SelectedTask](#selectedtask)
	* [vAddLevel_3](#vaddlevel_3)
	* [SelectedNoteBook](#selectednotebook)
	* [SelectedMeetingDuration](#selectedmeetingduration)
	* [AutoSelectMeeting](#autoselectmeeting)
	* [varGUID216](#varguid216)
	* [vAddLevel_1](#vaddlevel_1)
	* [ProgressBarPosition](#progressbarposition)
	* [vGUID208](#vguid208)
	* [SelectedMeeting](#selectedmeeting)
	* [vAddLevel_2](#vaddlevel_2)
	* [ShowDataLossWarning](#showdatalosswarning)
	* [PhotoNumber](#photonumber)
	* [V_ShowConfirm](#v_showconfirm)
	* [varGUID208](#varguid208)
	* [varLoadingPopup](#varloadingpopup)
	* [ExportConfirmed](#exportconfirmed)
	* [SketchNumber](#sketchnumber)
	* [SelectedImage](#selectedimage)
	* [IsLoading](#isloading)
	* [Loading](#loading)
	* [SelectedBucket](#selectedbucket)
	* [vContinue](#vcontinue)
	* [SelectedSection](#selectedsection)
	* [varSelectedPL](#varselectedpl)
	* [varDuplicatePopup](#varduplicatepopup)
	* [ShowTakenImage](#showtakenimage)
	* [varReviewTeam](#varreviewteam)
	* [AttachmentDeleteConfirm](#attachmentdeleteconfirm)
	* [FollowUpEnd](#followupend)
	* [varShowSort](#varshowsort)
	* [ShowPlanner](#showplanner)
	* [FollowUpConfirmed](#followupconfirmed)
	* [varGUID211](#varguid211)
	* [vFilter](#vfilter)
	* [vIsEdit](#visedit)
	* [ShowOverlay](#showoverlay)
	* [FollowUpStart](#followupstart)
	* [SelectedUser](#selecteduser)
	* [varAddMemo](#varaddmemo)
	* [EmailConfirmed](#emailconfirmed)
	* [varAddGoal](#varaddgoal)
	* [ShowImageSaved](#showimagesaved)
	* [SelectedPlan](#selectedplan)
	* [UserSelectedFromTasks](#userselectedfromtasks)
	* [vShowFilter](#vshowfilter)
	* [SecondsRemain](#secondsremain)
	* [UserSelected](#userselected)
	* [SelectedUserTasks](#selectedusertasks)
	* [myedit](#myedit)
	* [ShowOneNote](#showonenote)
	* [ varLoadingPopup](#-varloadingpopup)
	* [vGUID221](#vguid221)
	* [TaskSelected](#taskselected)
	* [MultiRecipients](#multirecipients)
	* [ShowSketchSaved](#showsketchsaved)
* [Global Collects](#global-collects)
	* [Tasks](#tasks)
	* [MeetingDurations](#meetingdurations)
	* [MeetingTimes](#meetingtimes)
	* [colQuestionRow](#colquestionrow)
	* [TempView_Plan](#tempview_plan)
	* [TempRi_Question](#tempri_question)
	* [TempPl_Allocation](#temppl_allocation)
	* [FollowUpMeetingAttendees](#followupmeetingattendees)
	* [OneNoteBooks](#onenotebooks)
	* [colPlDistribution](#colpldistribution)
	* [colDetailRow](#coldetailrow)
	* [Sketches](#sketches)
	* [MeetingAttendeesTemp](#meetingattendeestemp)
	* [colAnswerRow](#colanswerrow)
	* [TemplateData](#templatedata)
	* [colPlAssignment](#colplassignment)
	* [Templates](#templates)
	* [colAdTraegerCurrent](#coladtraegercurrent)
	* [colAdAssignment](#coladassignment)
	* [TempAu_Level_4](#tempau_level_4)
	* [colQuestionsAdd](#colquestionsadd)
	* [colAllocation](#colallocation)
	* [HoursList](#hourslist)
	* [TempRisk](#temprisk)
	* [EmailAttachments](#emailattachments)
	* [PlannerBuckets](#plannerbuckets)
	* [colFlowResponse](#colflowresponse)
	* [colPlDistributionCurrent](#colpldistributioncurrent)
	* [MeetingAttendeeEmails](#meetingattendeeemails)
	* [Photos](#photos)
	* [TempAu_Level_3](#tempau_level_3)
	* [PlannerPlans](#plannerplans)
	* [updateTable2201auGoals](#updatetable2201augoals)
	* [patchTable2011riDetail](#patchtable2011ridetail)
	* [TempPl_Goals](#temppl_goals)
	* [MeetingAttendees](#meetingattendees)
	* [Indexes](#indexes)
	* [OneNoteSections](#onenotesections)
	* [colAdRolle](#coladrolle)
	* [colModelRow](#colmodelrow)
	* [colAdTraeger](#coladtraeger)
	* [EmailRecipients](#emailrecipients)
* [Global Flows](#global-flows)
	* [weDit_SQL_runOperations](#wedit_sql_runoperations)
	* [weDit_SQL_modRiskAssessment](#wedit_sql_modriskassessment)
  
  

# Meeting Capture Demo


 An all-in-one meeting capture tool.

This tool helps you to keep everythin in one place during your meetings.

Key 
features are:
- View meeting details
- capture notes and pictures of whiteboards
- assign tasks
- send meeting notes to 
all attendees in one click

  

## OnStart


```
Collect(CalendarLocalizedLabel,      {Value:"Calendar"},{Value:"Kalender"},
{Value:"Təqvim"},{Value:"Kalendar"},{Value:"Calendari"},{Value:"Kalendář"},{Value:"Calendr"},{Value:"Calendario"},
{Value:"Egutegia"},{Value:"Kalendaryo"},{Value:"Calendrier"},{Value:"Féilire"},{Value:"Am mìosachan"},{Value:"Kalanda"},
{Value:"Dagbók"},{Value:"Kalenda"},{Value:"Kalendārs"},{Value:"Kalenner"},{Value:"Kalendorius"},{Value:"Naptár"},
{Value:"Kalendarju"},{Value:"Agenda"},{Value:"Taqvim"},{Value:"Kalendarz"},{Value:"Calendário"},{Value:"Intiwatana"},
{Value:"Kalendari"},{Value:"Kalendár"},{Value:"Koledar"},{Value:"Kalenteri"},{Value:"Maramataka"},{Value:"Lịch"},
{Value:"Takvim"},{Value:"Senenama"},{Value:"Ημερολόγιο"},{Value:"კალენდარი"},{Value:"לוח שנה"},{Value:"کیلنڈر"},
{Value:"التقويم"},{Value:"कैलेंडर"},{Value:"दिनदर्शिका"},{Value:"ক্যালেন্ডার"},{Value:"કૅલેન્ડર"},{Value:"予定表"},
{Value:"行事曆"},{Value:"日历"},{Value:"క్యాలెండర్"});

Concurrent(Set(MyCalendarID,LookUp(Office365Outlook.CalendarGetTables().value,DisplayName=LookUp(CalendarLocalizedLabel,Value=DisplayName).Value).Name);ClearCollect(AllFutureEvents,Office365Outlook.GetEventsCalendarView(MyCalendarID,Text(Today(),UTC),Text(DateAdd(Today(),2,Days),UTC)).Values),Set(MyUserProfile,Office365Users.MyProfile().Id),
    /*used to determine if meeting attendees are in app user's org*/
Set(MyDomain,Last(Split(User().Email,"@")).Result),
    /*used to determine countdown to end of selected meeting*/
Set(HomeTimerStart,Now()));
/*Meetings are defined to be calendar events less than 6 hours in length*/
ClearCollect(MeetingsOnly,Filter(AddColumns(AllFutureEvents,"isCurrent",DateDiff(Start,Now(),Seconds)>0&&DateDiff(Now(),End,Seconds)>0),DateDiff(Start,End,Hours)<6));Set(NumberOfCurrentMeetings,CountRows(Filter(MeetingsOnly,isCurrent)));
/*If a single meeting is happening now, autoselect it*/
If(NumberOfCurrentMeetings=1,Set(AutoSelectMeeting, true );Set(SelectedMeeting,LookUp(MeetingsOnly,isCurrent)))
```
# Connections
  
**OneNote (Business) (Standard)**  
  
sku: Enterprise  
  
With following datasources:  

- OneNote(Business)
  
  
**Planner (Standard)**  
  
sku: Enterprise  
  
With following datasources:  

- Planner
  
  
**Office 365-Benutzer (Standard)**  
  
sku: Enterprise  
  
With following datasources:  

- Office365Users
  
  
**Office 365 Outlook (Standard)**  
  
sku: Enterprise  
  
With following datasources:  

- Office365Outlook
  

# Screens
  
:::mermaid  
graph LR  
WelcomeScreen(WelcomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
HomeScreen(HomeScreen) --> SketchScreen(Sketch Screen)  
HomeScreen(HomeScreen) --> CameraScreen(CameraScreen)  
HomeScreen(HomeScreen) --> EmailScreen(EmailScreen)  
HomeScreen(HomeScreen) --> AttachmentsScreen(AttachmentsScreen)  
HomeScreen(HomeScreen) --> ExportScreen(ExportScreen)  
HomeScreen(HomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
SketchScreen(Sketch Screen) --> HomeScreen(HomeScreen)  
SketchScreen(Sketch Screen) --> CameraScreen(CameraScreen)  
CameraScreen(CameraScreen) --> HomeScreen(HomeScreen)  
CameraScreen(CameraScreen) --> SketchScreen(Sketch Screen)  
EmailScreen(EmailScreen) --> ConfirmScreen(ConfirmScreen)  
ConfirmScreen(ConfirmScreen) --> HomeScreen(HomeScreen)  
ConfirmScreen(ConfirmScreen) --> FollowUpScreen(FollowUpScreen)  
ConfirmScreen(ConfirmScreen) --> WelcomeScreen(WelcomeScreen)  
ExportScreen(ExportScreen) --> HomeScreen(HomeScreen)  
ExportScreen(ExportScreen) --> ExportPopUpsScreen(ExportPopUpsScreen)  
FollowUpScreen(FollowUpScreen) --> FollowUpTimesScreen(FollowUpTimesScreen)  
FollowUpTimesScreen(FollowUpTimesScreen) --> ConfirmScreen(ConfirmScreen)  
HomePopUpsScreen(HomePopUpsScreen) --> HomeScreen(HomeScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ExportScreen(ExportScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ConfirmScreen(ConfirmScreen)  
:::
## 2201_2
  
---
### Variables
  
Following variables have been created / or updated on this screen
- [vAddLevel_3](#vaddlevel_3)
- [varGUID216](#varguid216)
- [vAddLevel_1](#vaddlevel_1)
- [vGUID208](#vguid208)
- [vAddLevel_2](#vaddlevel_2)
- [V_ShowConfirm](#v_showconfirm)
- [varGUID208](#varguid208)
- [varLoadingPopup](#varloadingpopup)
- [IsLoading](#isloading)
- [vContinue](#vcontinue)
- [varDuplicatePopup](#varduplicatepopup)
- [varSelectedPL](#varselectedpl)
- [varReviewTeam](#varreviewteam)
- [varShowSort](#varshowsort)
- [varGUID211](#varguid211)
- [vFilter](#vfilter)
- [vIsEdit](#visedit)
- [varAddMemo](#varaddmemo)
- [varAddGoal](#varaddgoal)
- [vShowFilter](#vshowfilter)
- [myedit](#myedit)
- [varLoadingPopup](#varloadingpopup)
- [vGUID221](#vguid221)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [patchTable2011riDetail](#patchtable2011ridetail)
- [colQuestionRow](#colquestionrow)
- [TempPl_Allocation](#temppl_allocation)
- [colDetailRow](#coldetailrow)
- [colPlDistribution](#colpldistribution)
- [colAnswerRow](#colanswerrow)
- [colPlAssignment](#colplassignment)
- [colFlowResponse](#colflowresponse)
- [TempRi_Question](#tempri_question)
- [colAdTraegerCurrent](#coladtraegercurrent)
- [colAdAssignment](#coladassignment)
- [TempAu_Level_4](#tempau_level_4)
- [colQuestionsAdd](#colquestionsadd)
- [colAllocation](#colallocation)
- [colFlowResponse](#colflowresponse)
- [TempPl_Goals](#temppl_goals)
- [colPlDistributionCurrent](#colpldistributioncurrent)
- [TempAu_Level_3](#tempau_level_3)
- [TempView_Plan](#tempview_plan)
- [updateTable2201auGoals](#updatetable2201augoals)
- [patchTable2011riDetail](#patchtable2011ridetail)
- [TempPl_Allocation](#temppl_allocation)
- [TempPl_Goals](#temppl_goals)
- [colAdRolle](#coladrolle)
- [colModelRow](#colmodelrow)
- [colAdTraeger](#coladtraeger)
- [TempRisk](#temprisk)

### Flows
  
Following flows have used on this screen
- [weDit_SQL_modRiskAssessment](#wedit_sql_modriskassessment)
- [weDit_SQL_runOperations](#wedit_sql_runoperations)

### '2201_2' As screen

#### OnVisible


```
=//Warum kein Loading Spinner
//Concurrent prüfen

    Set(vContinue,false);
    Set(V_ShowConfirm,false);
    Set(vFilter,"Risk");

    //Collection prüfen
    Set(vAddLevel_1,false);
    Set(vAddLevel_2,false);
    Set(vAddLevel_3,false);

    Set(varAddGoal,false);

    //Dopplung der Collections prüfen
    ClearCollect(TempAu_Level_3, 'au.level_3');
    ClearCollect(TempAu_Level_4, 'au.level_4');

    Set(vGUID208,GUID());
    Set(vGUID221,GUID());
    ClearCollect(
        TempPl_Goals,
        AddColumns(
            Filter('pl.goals', fkey221 = varSelectedPL.ID221),
            "Edit",""
        )
    );
    ClearCollect(
        TempRisk,
        Filter('ri.detail', fkey208 = varSelectedPL.ID208)
    );
    ClearCollect(
        TempRi_Question,
        'ri.question'
    );
    ClearCollect(
        TempPl_Allocation,
        AddColumns(
            Filter('pl.allocation', fkey221 = varSelectedPL.ID221),
            "Edit","",
            "Surname", LookUp('ad.contact', ID281 = fkey281, Surname)
        )
    );
    Set(vShowFilter,false);
    UpdateContext(
        {
            locSortColumn: "pl_c_goals",
            locSortAscending: locSortColumn<>"pl_c_goals" Or !locSortAscending
        }
    )

//End concurrent

// Übernahme von ehemaligem Navigationsbutton 
Set(varAddMemo,false);
Clear(patchTable2011riDetail);
Set(varGUID211,LookUp('ri.version',And(fkey206 = varSelectedPL.fkey206,active=true),ID211));
Set(varGUID216,LookUp('ri.vDetail',And(active = true,fkey211 = varGUID211),fkey216));
If(IsBlankOrError(LookUp('ri.vDetail',And(fkey208 = varSelectedPL.fkey208,fkey211 = varGUID211,fkey216 =varGUID216),ID213)),
ClearCollect(colModelRow,Filter('ri.vModel',ID216 = varGUID216));
ClearCollect(colQuestionsAdd,Distinct(colModelRow,ID218));
ForAll(colQuestionsAdd,
Collect(patchTable2011riDetail,
Table({
ID213 : GUID(),
fkey208: varSelectedPL.fkey208,
fkey211: varGUID211,
fkey216: varGUID216,
fkey218: colQuestionsAdd[@Result],
fkey219: LookUp(colModelRow,ID218 = colQuestionsAdd[@Result],ID219),
ri_base: 0,
active: 1,
tableName: "[ri].[detail]",
fkey217: LookUp('ri.weight',And(fkey216 = varGUID216,fkey218 = colQuestionsAdd[@Result]),ID217),
type: "POST",
    UPN: User().Email})));
ClearCollect(colFlowResponse,weDit_SQL_runOperations.Run(JSON(patchTable2011riDetail, JSONFormat.IndentFour)));
Refresh('ri.vDetail');
Set(vFilter,"Risk");
ClearCollect(colDetailRow,Filter('ri.vDetail',And(fkey208 = varSelectedPL.fkey208,active = true)));
ClearCollect(colModelRow,Filter('ri.vModel',ID216 in colDetailRow.fkey216));
ClearCollect(colQuestionRow,AddColumns(Filter('ri.question',ID218 in colModelRow.ID218),"Edit",""));
ClearCollect(colAnswerRow,Filter('ri.answer',ID219 in colModelRow.ID219)),
Set(vFilter,"Risk");
Refresh('ri.vDetail');
ClearCollect(colDetailRow,Filter('ri.vDetail',And(fkey208 = varSelectedPL.fkey208,active = true)));
ClearCollect(colModelRow,Filter('ri.vModel',ID216 in colDetailRow.fkey216));
ClearCollect(colQuestionRow,AddColumns(Filter('ri.question',ID218 in colModelRow.ID218),"Edit",""));
ClearCollect(colAnswerRow,Filter('ri.answer',ID219 in colModelRow.ID219)))

```
### '2201_Memo-18_2' As text

### '2201_Risc-04_2' As gallery.variableTemplateHeightGallery

#### Items


```
=Sort(colQuestionRow,rq_count)
```
## WelcomeScreen
  
---  
:::mermaid  
graph LR  
WelcomeScreen(WelcomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
ConfirmScreen(ConfirmScreen) --> WelcomeScreen(WelcomeScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [ShowDataLossWarning](#showdatalosswarning)
- [FollowUpConfirmed](#followupconfirmed)
- [ExportConfirmed](#exportconfirmed)
- [AutoSelectMeeting](#autoselectmeeting)
- [SelectedMeeting](#selectedmeeting)
- [EmailConfirmed](#emailconfirmed)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [Templates](#templates)

### Flows
  
Following flows have used on this screen

### WelcomeScreen As screen


if any additional meeting is captured in the same session, guarantees all collections are empty
#### OnVisible


```
Clear(MeetingAttendees);
Clear(MeetingTimes);
Clear(EmailRecipients);
Clear(FollowUpMeetingAttendees);
Clear(Tasks);
Clear(Photos);
Clear(Sketches);
Clear(EmailAttachments);
Reset(NotesInput);
Reset(AssnTaskSearchUser_1);
Set(FollowUpConfirmed, false);
Set(EmailConfirmed, false);
Set(ExportConfirmed, false);

/*Email and OneNote templates with {placeholder} values for dynamic information*/

ClearCollect(Templates,
{Template: "Email", Value: "<!DOCTYPE html><html><head><title>" & "{MeetingName}" & "</title><style>div{box-sizing:border-box}table{table-layout:fixed;background-color:#eaedef;width:829px;font-family:'Open Sans',sans-serif;color:#2c3034}table.with-border td{border:2px solid #e3e3e3;background-color:#fff;vertical-align:top}td.caption{height:65px;background:#ed2955;color:#fff;text-align:center;vertical-align:middle}.details{font-size:14px;color:#2c3034;padding-top:10px}.header{font-size:16px;font-weight:600}.mark{font-weight:400;color:#617281}.name{font-size:12px;font-weight:600;color:#ed2955}table.no-border td.user-name{font-size:14px;font-weight:600;color:#2c3034;vertical-align:middle;height:20px;}.due-time{text-align:right;font-size:10px;vertical-align:middle;color:#617281;font-weight:400}.assign-to{font-size:12px;color:#617281}.job-title{font-size:12px;color:#4a4a4a;height:20px}table.no-border{width:100%}table.no-border td{border:0}table.no-border td.task{padding:10px 0;border-top:1px solid #f1f1f1}.user-img img{width:17px;height:19px;border:0;}.name a.link-name,.name a.link-name:visited{color:#ed2955;text-decoration:none;}</style></head><body><table border='0' cellpadding='0' cellspacing='0'><tr><td class='caption'>[ Meeting Capture ]</td></tr><tr><td style='border: 0;background-color: #eaedef;padding:30px 0 0 0;text-align: center;color: #2c3034;font-size: 20px;font-weight: 600;'>" & "{MeetingName}" & "</td></tr><tr><td style='border: 0;background-color: #eaedef;padding: 9px 0 10px 0;text-align: center;color: #2c3034;font-size: 14px;'>" & "{MeetingStartDate}" &" | " & "{MeetingStartTime}" & " - "& "{MeetingEndTime}" & " (" & "{MeetingMinutes}" & " Minutes)</td></tr></table><table class='with-border' border='0' cellpadding='20' cellspacing='20'><tr>
<td colspan='2' style='padding-bottom:10px;'><table border='0' cellpadding='0' cellspacing='0' class='no-border' style='table-layout:auto;'><tr><td colspan='3' class='header'>Attendees <span class='mark'>(" & "{MeetingAttendeeNum}" & ")</span></td></tr><tr><td colspan='3' style='height:10px;'></td></tr>" & "{1}" & "</table></td></tr><tr><td colspan='2'><table border='0' cellpadding='0' cellspacing='0' class='no-border'><tr><td class='header'>Meeting details</td></tr><tr><td class='details'>" & "{MeetingDetails}" & "</td></tr></table></td></tr><tr><td width='50%'><table border='0' cellpadding='0' cellspacing='0' class='no-border'><tr><td class='header'>Meeting Notes</td></tr><tr><td class='details'>" & "{MeetingNotes}" & "</td></tr></table></td><td width='50%'><table border='0' cellpadding='0' cellspacing='0' class='no-border'><tr><td class='header' style='padding-bottom:10px;'>Tasks</td></tr>" & "{2}" & "</table></td></tr><tr><td style='border:0;background-color:#eaedef;padding:0;height:10px;'></td></tr></table></body></html>"},
{Template: "OneNote", Value: "<!DOCTYPE html><html><head><title>" & "{MeetingName}" & "</title><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head><body data-absolute-enabled='true' style='font-family:Calibri;font-size:11pt'><div data-id='_default' style='position:absolute;left:48px;top:120px;width:829px;'><table border='0' cellpadding='0' cellspacing='0' width='829'><tr><td style='background-color:#ed2955;font-size:10pt;'>&nbsp;</td></tr><tr><td style='background-color:#ed2955;border:0px;text-align:center;font-weight:600;'><span style='color:white'>[ Meeting Capture ]</span></td></tr><tr><td style='background-color:#ed2955;font-size:8pt;'>&nbsp;</td></tr><tr><td style='background-color:#eaedef;font-size:14pt;'>&nbsp;</td></tr><tr><td style='background-color:#eaedef;border:0px;text-align:center;'><span style='font-size:15pt;color:#2c3034;font-weight:bold'>" & "{MeetingName}" & "</span></td></tr><tr><td style='background-color:#eaedef;border:0px;text-align:center;'><span style='font-size:10.5pt;color:#2c3034'>" & "{MeetingStartDate}" &" | " & "{MeetingStartTime}"&" - "& "{MeetingEndTime}" & " (" & "{MeetingMinutes}" & " Minutes)</span></td></tr><tr><td style='background-color:#eaedef;font-size:14pt;'>&nbsp;</td></tr><tr><td style='background-color:white;'><table border='0' cellpadding='0' cellspacing='0' width='829'><colgroup><col style='width: 210px;'><col style='width: 210px;'><col style='width: 210px;'><col style='width: 210px;'></colgroup><tr><td colspan='4' style='font-size:14pt;'><span style='font-weight:600;color:#2c3034'>Attendees</span>&nbsp;<span style='color:#617281'>(" & "{MeetingAttendeeNum}" & ")</span></td></tr>" & "{1}" & "</table></td></tr><tr><td style='background-color:#ffffff;font-size:8pt;'>&nbsp;</td></tr><tr><td style='background-color:#ffffff;font-size:8pt;'>&nbsp;</td></tr><tr><td style='background-color:white;'><table border='0' cellpadding='0' cellspacing='0' width='829'><tr><td width='420' style='font-size:14pt;font-weight:600;color:#2c3034'>Meeting Notes</td><td width='420' style='font-size:14pt;font-weight:600;color:#2c3034;border:10px solid red;'>Tasks</td></tr><tr><td style='font-size:12pt;color:#2c3034'>" & "{MeetingNotes}" & "</td><td style='font-size:14pt;font-weight:600;color:#2c3034'><table border='0' cellpadding='0' cellspacing='0' width='420'>" & "{2}" & "</table></td></tr></table></td></tr><tr><td style='background-color:#ffffff;font-size:8pt;'>&nbsp;</td></tr><tr><td style='background-color:white;'></td></tr><tr><td style='background-color:#eaedef;font-size:26.5pt;'>&nbsp;</td></tr></table></div></body></html>"})
```
### MeetingsGalleryBkg As button

#### OnSelect


```
=Select(Parent)
```
#### Text


```
=""
```
### BtnChangeAuto As button

#### OnSelect


```
=Set(AutoSelectMeeting, false)
```
#### Text


```
="Change"
```
## HomeScreen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> SketchScreen(Sketch Screen)  
HomeScreen(HomeScreen) --> CameraScreen(CameraScreen)  
HomeScreen(HomeScreen) --> EmailScreen(EmailScreen)  
HomeScreen(HomeScreen) --> AttachmentsScreen(AttachmentsScreen)  
HomeScreen(HomeScreen) --> ExportScreen(ExportScreen)  
HomeScreen(HomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
SketchScreen(Sketch Screen) --> HomeScreen(HomeScreen)  
CameraScreen(CameraScreen) --> HomeScreen(HomeScreen)  
ConfirmScreen(ConfirmScreen) --> HomeScreen(HomeScreen)  
ExportScreen(ExportScreen) --> HomeScreen(HomeScreen)  
HomePopUpsScreen(HomePopUpsScreen) --> HomeScreen(HomeScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [SelectedTask](#selectedtask)
- [UserSelectedFromTasks](#userselectedfromtasks)
- [SecondsRemain](#secondsremain)
- [FollowUpConfirmed](#followupconfirmed)
- [ExportConfirmed](#exportconfirmed)
- [UserSelected](#userselected)
- [SelectedUserTasks](#selectedusertasks)
- [ShowOverlay](#showoverlay)
- [TaskSelected](#taskselected)
- [ProgressBarPosition](#progressbarposition)
- [MultiRecipients](#multirecipients)
- [EmailConfirmed](#emailconfirmed)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [EmailRecipients](#emailrecipients)

### Flows
  
Following flows have used on this screen

### HomeScreen As screen


The main screen for meeting captures during a meeting.

- create meeting notes
- create tasks
- see meeting details

#### OnVisible


```
Set(FollowUpConfirmed, false);
Set(EmailConfirmed, false);
Set(ExportConfirmed, false)
```
### AppLogo1 As image

#### Image


```
='nav-logo'
```
### NavHome1 As image

#### Image


```
='nav-notes'
```
### NavSketch1 As image

#### Image


```
='nav-sketch'
```
#### OnSelect


```
=Navigate('Sketch Screen', None)
```
### NavPhotos1 As image

#### Image


```
='nav-camera'
```
#### OnSelect


```
=Navigate(CameraScreen, None)
```
### AttendeesBannerImage As image

#### Image


```
=attendees
```
### AttendeeGallery1 As gallery.galleryVertical

#### Items


```
=MeetingAttendees
```
### MailAllButton As button

#### OnSelect


```
=Navigate(EmailScreen, None);
Set(MultiRecipients, true);
ClearCollect(EmailRecipients, AttendeeGallery1.AllItems)
```
#### Text


```
="Email"
```
### NotesIcon As image

#### Image


```
=notes
```
### NotesInput As text

### Finish_SaveButton As button

#### OnSelect


```
=Navigate(ExportScreen, None)
```
#### Text


```
="Finish & Save"
```
### Finish_SaveIcon As image

#### Image


```
=export
```
#### OnSelect


```
=Select(Finish_SaveButton)
```
### TasksIcon As image

#### Image


```
=tasks
```
### TaskGallery As gallery.galleryVertical

#### Items


```
=Tasks
```
#### OnSelect


```
=If(CountRows(Tasks) > 0, 
Set(SelectedTask, ThisItem);
Set(TaskSelected, true);
Set(UserSelected, true);
Set(UserSelectedFromTasks, true);
Set(SelectedUserTasks, ThisItem.AssignToUser);
Set(ShowOverlay, true)
)
```
### TaskTitle As text

## Sketch Screen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> SketchScreen(Sketch Screen)  
SketchScreen(Sketch Screen) --> HomeScreen(HomeScreen)  
SketchScreen(Sketch Screen) --> CameraScreen(CameraScreen)  
CameraScreen(CameraScreen) --> SketchScreen(Sketch Screen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [SketchNumber](#sketchnumber)
- [ShowSketchSaved](#showsketchsaved)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [Sketches](#sketches)

### Flows
  
Following flows have used on this screen

### 'Sketch Screen' As screen


Create a sketch during a meeting.

The screen name "Sketch Screen" (notice the blank) akt's as a test for screen names 
with blank

#### OnVisible


```
Set(ShowSketchSaved, false)
```
### AppLogo2 As image

#### Image


```
='nav-logo'
```
### NavHome2 As image

#### Image


```
='nav-notes'
```
#### OnSelect


```
=Navigate(HomeScreen, None)
```
### NavSketch2 As image

#### Image


```
='nav-sketch'
```
### NavPhotos2 As image

#### Image


```
='nav-camera'
```
#### OnSelect


```
=Navigate(CameraScreen, None)
```
### SaveSketch As button

#### OnSelect


```
=/*store sketches in sketch collection*/
Set(SketchNumber, SketchNumber + 1);
Collect(Sketches, {Image:SketchCanvas.Image, Name: "Sketch" & SketchNumber & ".jpg"});
Reset(SketchCanvas);
Set(ShowSketchSaved, true)
```
#### Text


```
="Save sketch"
```
## CameraScreen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> CameraScreen(CameraScreen)  
SketchScreen(Sketch Screen) --> CameraScreen(CameraScreen)  
CameraScreen(CameraScreen) --> HomeScreen(HomeScreen)  
CameraScreen(CameraScreen) --> SketchScreen(Sketch Screen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [PhotoNumber](#photonumber)
- [ShowImageSaved](#showimagesaved)
- [ShowTakenImage](#showtakenimage)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [Photos](#photos)

### Flows
  
Following flows have used on this screen

### CameraScreen As screen


Take picture during a meeting
#### OnVisible


```
Set(ShowImageSaved, false);
Set(ShowTakenImage, false)
```
### AppLogo3 As image

#### Image


```
='nav-logo'
```
### NavHome3 As image

#### Image


```
='nav-notes'
```
#### OnSelect


```
=Navigate(HomeScreen, None)
```
### NavSketch3 As image

#### Image


```
='nav-sketch'
```
#### OnSelect


```
=Navigate('Sketch Screen', None)
```
### NavPhotos3 As image

#### Image


```
='nav-camera'
```
## EmailScreen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> EmailScreen(EmailScreen)  
EmailScreen(EmailScreen) --> ConfirmScreen(ConfirmScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [EmailConfirmed](#emailconfirmed)

### Collects
  
Following collects have been created, updated or cleared on this screen

### Flows
  
Following flows have used on this screen

### EmailScreen As screen


Email meeting notes to attendees
### AppLogo4 As image

#### Image


```
='nav-logo'
```
### SendEmail As button

#### OnSelect


```
=Office365Outlook.SendEmail(Concat(EmailRecipients, UserPrincipalName & ";"), EmailSubject.Text, EmailMessage.Text, {Importance: "Normal"});
/*Sets text to display email confirmation info*/
Set(EmailConfirmed, true);
Navigate(ConfirmScreen, None)
```
#### Text


```
="Send"
```
### GalleryBkg As button

#### Text


```
=""
```
### EmailRecipientGallery As gallery.galleryHorizontal

#### Items


```
=EmailRecipients
```
### EmailSubject As text

### EmailMessage As text

## AttachmentsScreen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> AttachmentsScreen(AttachmentsScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [AttachmentDeleteConfirm](#attachmentdeleteconfirm)
- [SelectedImage](#selectedimage)
- [ShowOverlay](#showoverlay)

### Collects
  
Following collects have been created, updated or cleared on this screen

### Flows
  
Following flows have used on this screen

### AttachmentsScreen As screen


See attachments created during meeting
### AppLogo5 As image

#### Image


```
='nav-logo'
```
### PhotosIcon As image

#### Image


```
='attachments-camera'
```
### PhotosGallery As gallery.galleryHorizontal

#### Items


```
=Photos
```
#### OnSelect


```
=Set(ShowOverlay, true);
Set(SelectedImage, ThisItem)
```
### SketchesIcon As image

#### Image


```
='attachments-sketch'
```
### SketchesGallery As gallery.galleryHorizontal

#### Items


```
=Sketches
```
#### OnSelect


```
=Set(ShowOverlay, true);
Set(SelectedImage, ThisItem)
```
### AttachmentToDelete As image

#### Image


```
=SelectedImage.Image
```
### CancelDeleteAttach As button

#### OnSelect


```
=Set(AttachmentDeleteConfirm, false);
Set(ShowOverlay, false)
```
#### Text


```
=If(TaskSelected, "Delete", "Cancel")
```
### ConfirmDeleteAttach As button

#### OnSelect


```
=Set(ShowOverlay, false);
Set(AttachmentDeleteConfirm, false);
RemoveIf(Sketches, SelectedImage.Name = Name);
RemoveIf(Photos, SelectedImage.Name = Name)

```
#### Text


```
="Yes, delete"
```
## ConfirmScreen
  
---  
:::mermaid  
graph LR  
EmailScreen(EmailScreen) --> ConfirmScreen(ConfirmScreen)  
ConfirmScreen(ConfirmScreen) --> HomeScreen(HomeScreen)  
ConfirmScreen(ConfirmScreen) --> FollowUpScreen(FollowUpScreen)  
ConfirmScreen(ConfirmScreen) --> WelcomeScreen(WelcomeScreen)  
FollowUpTimesScreen(FollowUpTimesScreen) --> ConfirmScreen(ConfirmScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ConfirmScreen(ConfirmScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [Loading](#loading)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [EmailAttachments](#emailattachments)
- [Indexes](#indexes)
- [TemplateData](#templatedata)

### Flows
  
Following flows have used on this screen

### ConfirmScreen As screen


Export confirmation screen
Once the export is completed another meeting can be scheduled with the attendees.

#### OnVisible


```
If(ExportConfirmed,
    Set(Loading, true);

    /*Collects the dynamic data which will be substituted into the Email/OneNote templates and associates it to the {placeholder} values in the templates
       At {Field: "{1}" at <tr><td colspan='3'> changed <td colspan='3' style='height:10px;'> to <td colspan='3'> because OneNote stopped displaying the export content with the inline style content present 
    */
        If(CheckEmail.Value || CheckOneNote.Value, 
             ClearCollect(TemplateData, {Field:"{MeetingName}", Data:SelectedMeeting.Subject}, {Field: "{MeetingStartDate}", Data: Text(SelectedMeeting.Start, "[$-en-US]mmm. dd, yyyy")}, 
            {Field: "{MeetingStartTime}", Data: Lower(Text(SelectedMeeting.Start, "[$-en-US]hh:mm am/pm"))}, {Field: "{MeetingEndTime}", Data: Lower(Text(SelectedMeeting.End, "[$-en-US]hh:mm am/pm"))},
            {Field: "{MeetingMinutes}", Data: Text(SelectedMeetingDuration/60)}, {Field: "{MeetingAttendeeNum}", Data: Text(CountRows(MeetingAttendees))},
            {Field: "{1}", 
            Data: Concat(
                GroupBy(
                    ForAll(MeetingAttendees,
                        Collect(Indexes, {Index:Last(Indexes).Index + 1});
                        {Page:RoundDown(Last(Indexes).Index / 3,0),
                        Id:Id, 
                        DisplayName:DisplayName, 
                        JobTitle:JobTitle}
                    ),
            "Page","Attendees"),"<tr>" & Concat(Attendees,"<td class='user-name' width='221'>" & DisplayName & "</td>") & If(CountRows(Attendees)=2,"<td class='user-name' width='221'></td>",CountRows(Attendees)=1,
            "<td class='user-name' width='221'></td><td class='user-name' width='221'></td>") & "</tr><tr>" & Concat(Attendees,"<td class='job-title'>" & JobTitle & "</td>") & If(CountRows(Attendees)=2,
            "<td class='job-title'></td>",CountRows(Attendees)=1,"<td class='job-title'></td><td class='job-title'></td>") & "</tr><tr><td colspan='3'></td></tr>")},
            {Field: "{MeetingDetails}", Data:MeetingBody.HtmlText}, {Field: "{MeetingNotes}", Data: Substitute(NotesInput.Text, Char(10), "<br/>")},
            {Field: "{2}", Data: Concat(Tasks,"<tr><td class='task'><table border='0' cellpadding='0' cellspacing='0' class='no-border' style='table-layout:auto'><tr><td class='name'><a class='link-name' href='https://tasks.office.com' target='_blank'>" & Name & "</a></td><td class='due-time'>" & If(IsBlank(DueDate),"","Due " & If(IsToday(DueDate),"Today",Text(DueDate,"[$-en-US]mmm d"))) & "</td></tr><tr><td colspan='2' class='assign-to'>" & AssignToUser.DisplayName & "</td></tr></table></td></tr>")})
        );

        /*Creates planner tasks based on the Tasks collection*/
        If(CheckPlanner.Value,ForAll(Tasks,Planner.CreateTask(SelectedPlan.'data-ADB4D7A662F548B49FAC2B986E348A1Bid',Name,{bucketId:SelectedBucket.'data-ADB4D7A662F548B49FAC2B986E348A1Bid',dueDateTime:AssnTaskDueDate_1,assignments:AssignToUser.Id})));
        /*combines photos and sketches into a single email attachments collection*/
        If(CheckEmail.Value,
            ForAll(Photos, Collect(EmailAttachments, {ContentBytes: Image, Image: Image, Name: Name}));
            ForAll(Sketches, Collect(EmailAttachments, {ContentBytes: Image, Image: Image, Name: Name}));
        /*replaces {placeholder} values for Email template with dynamic data collected from user's input as they progress through app*/   
            ForAll(TemplateData, Patch(Templates, LookUp(Templates, Template="Email"), {Value: Substitute(LookUp(Templates, Template="Email").Value, Field, Data)}));
            Office365Outlook.SendEmail(Concat(EmailRecipients, UserPrincipalName & ";"), SelectedMeeting.Subject, LookUp(Templates, Template="Email").Value, {Attachments: EmailAttachments, Importance: "Normal", IsHtml: true}
            )    
        );
        If(CheckOneNote.Value,
        /*replaces {placeholder} values for OneNote template with dynamic data collected from user's input as they progress through app*/    
            ForAll(TemplateData, Patch(Templates, LookUp(Templates, Template="OneNote"), {Value: Substitute(LookUp(Templates, Template="OneNote").Value, Field, Data)}));
            'OneNote(Business)'.CreatePageInSection(SelectedNoteBook.'data-ADB4D7A662F548B49FAC2B986E348A1BKey', SelectedSection.'data-ADB4D7A662F548B49FAC2B986E348A1BpagesUrl', LookUp(Templates, Template="OneNote").Value)
        );

    Set(Loading, false)
)
```
## ExportScreen
  
---  
:::mermaid  
graph LR  
HomeScreen(HomeScreen) --> ExportScreen(ExportScreen)  
ExportScreen(ExportScreen) --> HomeScreen(HomeScreen)  
ExportScreen(ExportScreen) --> ExportPopUpsScreen(ExportPopUpsScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ExportScreen(ExportScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [SelectedPlan](#selectedplan)
- [ShowPlanner](#showplanner)
- [ShowOneNote](#showonenote)
- [SelectedNoteBook](#selectednotebook)
- [SelectedBucket](#selectedbucket)
- [ShowOverlay](#showoverlay)
- [SelectedSection](#selectedsection)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [OneNoteSections](#onenotesections)
- [PlannerBuckets](#plannerbuckets)
- [PlannerPlans](#plannerplans)
- [EmailRecipients](#emailrecipients)
- [OneNoteBooks](#onenotebooks)

### Flows
  
Following flows have used on this screen

### ExportScreen As screen


Export creation screen
Select where to export to.
Possible exports:
- OneNote
- Office Planner
- Email

#### OnVisible


```
If(IsEmpty(EmailRecipients), 
    ClearCollect(EmailRecipients, AttendeeGallery1.AllItems)
);
If(IsEmpty(OneNoteBooks), ClearCollect(OneNoteBooks,'OneNote(Business)'.GetNotebooks()));
If(!IsEmpty(OneNoteBooks),ClearCollect(OneNoteSections,'OneNote(Business)'.GetSectionsInNotebook(OneNoteBookSelect_1.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1BKey').value));
If(IsEmpty(PlannerPlans), ClearCollect(PlannerPlans, Planner.ListMyPlans().value));
If(!IsEmpty(PlannerPlans),ClearCollect(PlannerBuckets,Planner.ListBuckets(PlannerPlanSelect_1.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1Bid').value))
```
### AppLogo7 As image

#### Image


```
='nav-logo'
```
### ExportButton As button

#### OnSelect


```
=Set(ShowOverlay, true);
Navigate(ExportPopUpsScreen, None)
```
#### Text


```
="Export"
```
### ExportIcon As image

#### Image


```
=export
```
#### OnSelect


```
=Select(ExportButton)
```
### OneNoteIcon As image

#### Image


```
='one-note'
```
### ShowOneNoteSelection As button

#### OnSelect


```
=Set(ShowOneNote, true);
Navigate(ExportPopUpsScreen, None);
/*retrieves OneNote sections of (pre)selected OneNote book (if user hasn't selected one yet)*/
ClearCollect(OneNoteSections, 'OneNote(Business)'.GetSectionsInNotebook(OneNoteBookSelect_1.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1BKey').value)
```
#### Text


```
=If(ExportToOneNote.Height > 0, "Select new location", "Select Location")
```
### EmailIcon As image

#### Image


```
=outlook
```
### RecipientGalleryBkg As button

#### Text


```
=""
```
### EmailRecipientsGallery As gallery.galleryVertical

#### Items


```
=EmailRecipients
```
### AssnTaskSearchUser_1 As text

### UserSearchResults As gallery.galleryVertical

#### Items


```
=If(!IsBlank(AssnTaskSearchUser_1.Text), Office365Users.SearchUser({searchTerm:Trim(AssnTaskSearchUser_1.Text), top:15}))
```
#### OnSelect


```
=If(Not(ThisItem.Id in EmailRecipients.Id), Collect(EmailRecipients, ThisItem))
```
### PlannerIcon As image

#### Image


```
=planner
```
### ShowPlannerSelection As button

#### OnSelect


```
=Set(ShowPlanner, true);
Navigate(ExportPopUpsScreen, None)
```
#### Text


```
=If(PlannerExportTo.Height > 0, "Select new location", "Select Location")
```
## FollowUpScreen
  
---  
:::mermaid  
graph LR  
ConfirmScreen(ConfirmScreen) --> FollowUpScreen(FollowUpScreen)  
FollowUpScreen(FollowUpScreen) --> FollowUpTimesScreen(FollowUpTimesScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [ExportConfirmed](#exportconfirmed)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [FollowUpMeetingAttendees](#followupmeetingattendees)

### Flows
  
Following flows have used on this screen

### FollowUpScreen As screen


Schedule follow up for this meeting
#### OnVisible


```
Set(ExportConfirmed, false);
ClearCollect(FollowUpMeetingAttendees, MeetingAttendees)
```
### AppIcon7 As image

#### Image


```
='nav-logo'
```
### FindAvailableTimesButton As button

#### OnSelect


```
=Navigate(FollowUpTimesScreen, None)
```
#### Text


```
="Find Available Times"
```
### FollowUpGallBkg As button

#### Text


```
=""
```
### FollowUpAttendeesGall As gallery.galleryVertical

#### Items


```
=FollowUpMeetingAttendees
```
### FollowUpSearchText As text

### FollowUpSearchUserResults As gallery.galleryVertical

#### Items


```
=If(!IsBlank(FollowUpSearchText.Text), Office365Users.SearchUser({searchTerm:Trim(FollowUpSearchText.Text), top:15}))
```
#### OnSelect


```
=If(Not(ThisItem.Id in FollowUpMeetingAttendees.Id), Collect(FollowUpMeetingAttendees, ThisItem))
```
### FollowUpSubject As text

### FollowUpMessage As text

## FollowUpTimesScreen
  
---  
:::mermaid  
graph LR  
FollowUpScreen(FollowUpScreen) --> FollowUpTimesScreen(FollowUpTimesScreen)  
FollowUpTimesScreen(FollowUpTimesScreen) --> ConfirmScreen(ConfirmScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [ShowMeetingTimes](#showmeetingtimes)
- [FollowUpEnd](#followupend)
- [FollowUpConfirmed](#followupconfirmed)
- [Loading](#loading)
- [FollowUpStart](#followupstart)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [MeetingDurations](#meetingdurations)
- [MeetingTimes](#meetingtimes)
- [HoursList](#hourslist)

### Flows
  
Following flows have used on this screen

### FollowUpTimesScreen As screen


Collections used in galleries and drop downs on this screen
- MeetingDurations
- HoursList

#### OnVisible


```
ClearCollect(MeetingDurations,
{Name:"30 minutes", Minutes:30},{Name:"1 hour", Minutes:60},{Name:"90 minutes", Minutes:90},{Name:"2 hours", Minutes:120},
{Name:"2.5 hours", Minutes:150},{Name:"3 hours", Minutes:180},{Name:"3.5 hours", Minutes:210},{Name:"4 hours", Minutes:240});

ClearCollect(HoursList, {Name:"12:00 am",Minutes:0}, {Name:"12:30 am",Minutes:30}, {Name:"01:00 am",Minutes:60}, {Name:"01:30 am",Minutes:90}, {Name:"02:00 am",Minutes:120}, {Name:"02:30 am",Minutes:150}, {Name:"03:00 am",Minutes:180}, {Name:"03:30 am",Minutes:210}, {Name:"04:00 am",Minutes:240, Short: "4 am"}, {Name:"04:30 am",Minutes:270}, {Name:"05:00 am",Minutes:300}, {Name:"05:30 am",Minutes:330}, {Name:"06:00 am",Minutes:360}, {Name:"06:30 am",Minutes:390}, {Name:"07:00 am",Minutes:420}, {Name:"07:30 am",Minutes:450}, {Name:"08:00 am",Minutes:480, Short: "8 am"}, {Name:"08:30 am",Minutes:510}, {Name:"09:00 am",Minutes:540}, {Name:"09:30 am",Minutes:570}, {Name:"10:00 am",Minutes:600}, {Name:"10:30 am",Minutes:630}, {Name:"11:00 am",Minutes:660}, {Name:"11:30 am",Minutes:690}, {Name:"12:00 pm",Minutes:720, Short: "12 pm"
}, {Name:"12:30 pm",Minutes:750}, {Name:"01:00 pm",Minutes:780}, {Name:"01:30 pm",Minutes:810}, {Name:"02:00 pm",Minutes:840}, {Name:"02:30 pm",Minutes:870}, {Name:"03:00 pm",Minutes:900}, {Name:"03:30 pm",Minutes:930}, {Name:"04:00 pm",Minutes:960, Short: "4 pm"}, {Name:"04:30 pm",Minutes:990}, {Name:"05:00 pm",Minutes:1020}, {Name:"05:30 pm",Minutes:1050}, {Name:"06:00 pm",Minutes:1080}, {Name:"06:30 pm",Minutes:1110}, {Name:"07:00 pm",Minutes:1140}, {Name:"07:30 pm",Minutes:1170}, {Name:"08:00 pm",Minutes:1200, Short: "8 pm"}, {Name:"08:30 pm",Minutes:1230}, {Name:"09:00 pm",Minutes:1260}, {Name:"09:30 pm",Minutes:1290}, {Name:"10:00 pm",Minutes:1320}, {Name:"10:30 pm",Minutes:1350}, {Name:"11:00 pm",Minutes:1380}, {Name:"11:30 pm",Minutes:1410})
```
### AppIcon8 As image

#### Image


```
='nav-logo'
```
### SendInvite As button

#### OnSelect


```
=/*creates calendar event for meeting*/
UpdateContext({requiredAttendees:Concat(FollowUpMeetingAttendees, UserPrincipalName & ";")});
UpdateContext({requiredAttendees:Left(requiredAttendees, Len(requiredAttendees)-1)});
Office365Outlook.V4CalendarPostItem(MyCalendarID, FollowUpSubject.Text, FollowUpStart, FollowUpEnd, "UTC",{importance:"Normal", body:FollowUpMessage.Text, showAs:"busy", requiredAttendees:requiredAttendees});
Set(FollowUpConfirmed, true);
Navigate(ConfirmScreen,None)
```
#### Text


```
="Send Invite"
```
### LoadAvailableTimes As button

#### OnSelect


```
=Set(Loading, true);
/*
Collects available meeting times for attendees based on user determined data from this page. Adds 'StartTime' and 'EndTime' columns to the collection as a means of simplifying the MeetingTimeSlot column
*/
ClearCollect(MeetingTimes,AddColumns(Office365Outlook.FindMeetingTimes({MaxCandidates:15,MinimumAttendeePercentage: 1, MeetingDuration: MeetingDurationSelection.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1BMinutes',Start:Text(DateAdd(DatePicker1.SelectedDate,MeetingStartRange.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1BMinutes', Minutes), UTC),End:Text(DateAdd(DatePicker1.SelectedDate, MeetingEndRange.SelectedText.'data-ADB4D7A662F548B49FAC2B986E348A1BMinutes', Minutes), UTC),RequiredAttendees:Concat(FollowUpMeetingAttendees,UserPrincipalName & ";")}).MeetingTimeSuggestions,"StartTime",MeetingTimeSlot.Start.DateTime,
"EndTime",MeetingTimeSlot.End.DateTime));
Set(ShowMeetingTimes, true);
Set(Loading, false)
```
#### Text


```
="Find Available Times"
```
### TimeLine As gallery.galleryHorizontal

#### Items


```
=HoursList
```
### AvailableTimesGall As gallery.galleryVertical

#### Items


```
=SortByColumns(MeetingTimes,"Confidence",Descending,"StartTime",Ascending)
```
## HomePopUpsScreen
  
---  
:::mermaid  
graph LR  
WelcomeScreen(WelcomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
HomeScreen(HomeScreen) --> HomePopUpsScreen(HomePopUpsScreen)  
HomePopUpsScreen(HomePopUpsScreen) --> HomeScreen(HomeScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [ShowDataLossWarning](#showdatalosswarning)
- [UserSelectedFromTasks](#userselectedfromtasks)
- [UserSelected](#userselected)
- [SelectedMeetingDuration](#selectedmeetingduration)
- [Loading](#loading)
- [ShowOverlay](#showoverlay)
- [TaskSelected](#taskselected)
- [SelectedUser](#selecteduser)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [MeetingAttendeesTemp](#meetingattendeestemp)
- [MeetingAttendeeEmails](#meetingattendeeemails)
- [MeetingAttendees](#meetingattendees)
- [Tasks](#tasks)

### Flows
  
Following flows have used on this screen

### HomePopUpsScreen As screen


Gathers and stores the Office 365 profiles of the meeting attendees if they are within the app user's org
#### OnVisible


```
If(IsEmpty(MeetingAttendees),
    Set(Loading, true);
    ClearCollect(MeetingAttendeeEmails, Filter(Split(Concatenate(SelectedMeeting.RequiredAttendees,
     SelectedMeeting.OptionalAttendees), ";"), Result <> ""));
    ClearCollect(MeetingAttendeesTemp, ForAll(MeetingAttendeeEmails, If(Lower(MyDomain) = Lower(Last(Split(Result, "@")).Result), Office365Users.UserProfileV2(Result), {displayName: Result, id: "", image: Blank(), jobTitle: "", userPrincipalName: Result})));
    ClearCollect(MeetingAttendees, RenameColumns(MeetingAttendeesTemp, "id", "Id", "jobTitle", "JobTitle", "displayName", "DisplayName", "userPrincipalName", "UserPrincipalName"));
    Set(SelectedMeetingDuration, DateDiff(SelectedMeeting.Start, SelectedMeeting.End, Seconds));
    Set(Loading, false)
)
```
### AssnTaskDescription_1 As text

### AssnTaskGallery_2 As gallery.galleryVertical

#### Items


```
=/*
In-org attendee gallery for task assignment
If the attendee DisplayName is an actual name and not an email address, then they are in the app user's org, so we can assign them a task.
Tasks are stored in an 0365 tenant, so cannot be assigned to external users
*/
Filter(AttendeeGallery1.AllItems, Not(".com" in DisplayName))
```
#### OnSelect


```
=If(AssnTaskGallery_2.Visible,
    Set(UserSelected, true);
    Set(SelectedUser, {DisplayName:AssnTaskGallery_2.Selected.DisplayName, Id:AssnTaskGallery_2.Selected.Id, Image: AssnTaskGallery_2.Selected.AssnTaskUserImg_3.Image, JobTitle:AssnTaskGallery_2.Selected.JobTitle})
)
```
### AssnTaskSearchUser_2 As text

### CancelAssnTask_1 As button

#### OnSelect


```
=Navigate(HomeScreen, None);
Set(ShowOverlay, !ShowOverlay);
If(TaskSelected, RemoveIf(Tasks, Id = SelectedTask.Id));
Set(UserSelected, false);
Set(UserSelectedFromTasks, false);
Set(TaskSelected, false);
Reset(AssnTaskSearchUser_2);
Reset(AssnTaskDueDate_1);
Reset(AssnTaskDescription_1);
Reset(TaskTitle)
```
#### Text


```
=If(TaskSelected, "Delete", "Cancel")
```
### SaveAssnTask_1 As button

#### OnSelect


```
=Navigate(HomeScreen, None);
Set(ShowOverlay, !ShowOverlay);
/*If user is making a new task, collect the information from form, otherwise, revise the task the user is editing*/
If(!TaskSelected,
    Collect(Tasks, {Id: CountRows(Tasks)+1, Name:AssnTaskDescription_1.Text, DueDate: AssnTaskDueDate_1.SelectedDate, 
AssignToUser: SelectedUser}),
    Patch(Tasks, LookUp(Tasks, Id=SelectedTask.Id), {Name:AssnTaskDescription_1.Text, DueDate: AssnTaskDueDate_1.SelectedDate, AssignToUser: SelectedUser}));
Set(UserSelected, false);
Set(UserSelectedFromTasks, false);
Set(TaskSelected, false);
Reset(AssnTaskSearchUser_2);
Reset(AssnTaskDueDate_1);
Reset(AssnTaskDescription_1);
Reset(TaskTitle)
```
#### Text


```
="Save task"
```
### AssnTaskGallery_3 As gallery.galleryVertical

#### Items


```
=/*User search gallery*/
If(!IsBlank(AssnTaskSearchUser_2.Text), Office365Users.SearchUser({searchTerm:Trim(AssnTaskSearchUser_2.Text), top:15}))
```
#### OnSelect


```
=Set(SelectedUser, {DisplayName:AssnTaskGallery_3.Selected.DisplayName, Id:AssnTaskGallery_3.Selected.Id, Image: AssnTaskGallery_3.Selected.AssnTaskUserImg_4.Image, JobTitle:AssnTaskGallery_3.Selected.JobTitle});
Set(UserSelected, true)
```
### AssnTaskUserImg_5 As image

#### Image


```
=If(UserSelectedFromTasks,SelectedUserTasks.Image,SelectedUser.Image)
```
#### OnSelect


```
=
```
### DataWarningAccept_1 As button

#### OnSelect


```
=Set(ShowDataLossWarning, false);
Navigate(HomeScreen, None)
```
#### Text


```
="Got it!"
```
## ExportPopUpsScreen
  
---  
:::mermaid  
graph LR  
ExportScreen(ExportScreen) --> ExportPopUpsScreen(ExportPopUpsScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ExportScreen(ExportScreen)  
ExportPopUpsScreen(ExportPopUpsScreen) --> ConfirmScreen(ConfirmScreen)  
:::
### Variables
  
Following variables have been created / or updated on this screen
- [SelectedPlan](#selectedplan)
- [ShowPlanner](#showplanner)
- [ExportConfirmed](#exportconfirmed)
- [ShowOneNote](#showonenote)
- [SelectedNoteBook](#selectednotebook)
- [SelectedBucket](#selectedbucket)
- [ShowOverlay](#showoverlay)
- [SelectedSection](#selectedsection)

### Collects
  
Following collects have been created, updated or cleared on this screen
- [OneNoteSections](#onenotesections)
- [PlannerBuckets](#plannerbuckets)

### Flows
  
Following flows have used on this screen

### ExportPopUpsScreen As screen

### ExportCancel_1 As button

#### OnSelect


```
=Set(ShowOneNote, false);
Set(ShowPlanner, false);
Set(ShowOverlay, false);
Navigate(ExportScreen, None)
```
#### Text


```
=If(TaskSelected, "Delete", "Cancel")
```
### ExportConfirm_1 As button

#### OnSelect


```
=If(ShowOneNote,
    Set(ShowOneNote, false);
    Set(SelectedNoteBook, OneNoteBookSelect_1.SelectedText);
    Set(SelectedSection, SectionsSelect_1.SelectedText);
    Navigate(ExportScreen, None),
   ShowPlanner,
    Set(ShowPlanner, false);
    Set(SelectedPlan, PlannerPlanSelect_1.SelectedText);
    Set(SelectedBucket, PlannerBucketSelect_1.SelectedText);
    Navigate(ExportScreen, None),
   ShowOverlay,
    Set(ShowOverlay, false);
    Set(ExportConfirmed, true);
    Navigate(ConfirmScreen, None)
)

```
#### Text


```
=If(ShowOverlay, "Yes, continue", "OK")
```
## CollectionsAndVariables
  
---
### Variables
  
Following variables have been created / or updated on this screen

### Collects
  
Following collects have been created, updated or cleared on this screen

### Flows
  
Following flows have used on this screen

### CollectionsAndVariables As screen


This screen lists all collections and variables used inside the app

## TestEmptyScreen
  
---
### Variables
  
Following variables have been created / or updated on this screen

### Collects
  
Following collects have been created, updated or cleared on this screen

### Flows
  
Following flows have used on this screen

### TestEmptyScreen As screen

# Global Variables
  
Usage of global variables is shown based on the screen(s) where this variable is set and the screen(s) where it is used.
 
## ShowMeetingTimes
  
:::mermaid  
graph LR  
SetFollowUpTimesScreen(FollowUpTimesScreen)-- set -->ShowMeetingTimes[/ShowMeetingTimes/]  
ShowMeetingTimes[/ShowMeetingTimes/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
ShowMeetingTimes[/ShowMeetingTimes/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedTask
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->SelectedTask[/SelectedTask/]  
SelectedTask[/SelectedTask/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
SelectedTask[/SelectedTask/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## vAddLevel_3
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vAddLevel_3[/vAddLevel_3/]  
:::
## SelectedNoteBook
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->SelectedNoteBook[/SelectedNoteBook/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->SelectedNoteBook[/SelectedNoteBook/]  
SelectedNoteBook[/SelectedNoteBook/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedNoteBook[/SelectedNoteBook/]-. use .->UseExportScreen(ExportScreen)  
SelectedNoteBook[/SelectedNoteBook/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedMeetingDuration
  
:::mermaid  
graph LR  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->SelectedMeetingDuration[/SelectedMeetingDuration/]  
SelectedMeetingDuration[/SelectedMeetingDuration/]-. use .->UseHomeScreen(HomeScreen)  
SelectedMeetingDuration[/SelectedMeetingDuration/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedMeetingDuration[/SelectedMeetingDuration/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## AutoSelectMeeting
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->AutoSelectMeeting[/AutoSelectMeeting/]  
AutoSelectMeeting[/AutoSelectMeeting/]-. use .->UseWelcomeScreen(WelcomeScreen)  
AutoSelectMeeting[/AutoSelectMeeting/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varGUID216
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varGUID216[/varGUID216/]  
varGUID216[/varGUID216/]-. use .->Use2201_2(2201_2)  
:::
## vAddLevel_1
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vAddLevel_1[/vAddLevel_1/]  
:::
## ProgressBarPosition
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->ProgressBarPosition[/ProgressBarPosition/]  
ProgressBarPosition[/ProgressBarPosition/]-. use .->UseHomeScreen(HomeScreen)  
ProgressBarPosition[/ProgressBarPosition/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## vGUID208
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vGUID208[/vGUID208/]  
:::
## SelectedMeeting
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->SelectedMeeting[/SelectedMeeting/]  
SelectedMeeting[/SelectedMeeting/]-. use .->UseWelcomeScreen(WelcomeScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseHomeScreen(HomeScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseEmailScreen(EmailScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseExportScreen(ExportScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseFollowUpScreen(FollowUpScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
SelectedMeeting[/SelectedMeeting/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## vAddLevel_2
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vAddLevel_2[/vAddLevel_2/]  
:::
## ShowDataLossWarning
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->ShowDataLossWarning[/ShowDataLossWarning/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->ShowDataLossWarning[/ShowDataLossWarning/]  
ShowDataLossWarning[/ShowDataLossWarning/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
ShowDataLossWarning[/ShowDataLossWarning/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## PhotoNumber
  
:::mermaid  
graph LR  
SetCameraScreen(CameraScreen)-- set -->PhotoNumber[/PhotoNumber/]  
PhotoNumber[/PhotoNumber/]-. use .->UseCameraScreen(CameraScreen)  
PhotoNumber[/PhotoNumber/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## V_ShowConfirm
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->V_ShowConfirm[/V_ShowConfirm/]  
:::
## varGUID208
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varGUID208[/varGUID208/]  
:::
## varLoadingPopup
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varLoadingPopup[/varLoadingPopup/]  
varLoadingPopup[/varLoadingPopup/]-. use .->Use2201_2(2201_2)  
:::
## ExportConfirmed
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->ExportConfirmed[/ExportConfirmed/]  
SetHomeScreen(HomeScreen)-- set -->ExportConfirmed[/ExportConfirmed/]  
SetFollowUpScreen(FollowUpScreen)-- set -->ExportConfirmed[/ExportConfirmed/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->ExportConfirmed[/ExportConfirmed/]  
ExportConfirmed[/ExportConfirmed/]-. use .->UseConfirmScreen(ConfirmScreen)  
ExportConfirmed[/ExportConfirmed/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SketchNumber
  
:::mermaid  
graph LR  
SetSketchScreen(Sketch Screen)-- set -->SketchNumber[/SketchNumber/]  
SketchNumber[/SketchNumber/]-. use .->UseSketchScreen(Sketch Screen)  
SketchNumber[/SketchNumber/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedImage
  
:::mermaid  
graph LR  
SetAttachmentsScreen(AttachmentsScreen)-- set -->SelectedImage[/SelectedImage/]  
SelectedImage[/SelectedImage/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
SelectedImage[/SelectedImage/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## IsLoading
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->IsLoading[/IsLoading/]  
:::
## Loading
  
:::mermaid  
graph LR  
SetConfirmScreen(ConfirmScreen)-- set -->Loading[/Loading/]  
SetFollowUpTimesScreen(FollowUpTimesScreen)-- set -->Loading[/Loading/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->Loading[/Loading/]  
Loading[/Loading/]-. use .->Use2201_2(2201_2)  
Loading[/Loading/]-. use .->UseWelcomeScreen(WelcomeScreen)  
Loading[/Loading/]-. use .->UseHomeScreen(HomeScreen)  
Loading[/Loading/]-. use .->UseEmailScreen(EmailScreen)  
Loading[/Loading/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
Loading[/Loading/]-. use .->UseConfirmScreen(ConfirmScreen)  
Loading[/Loading/]-. use .->UseExportScreen(ExportScreen)  
Loading[/Loading/]-. use .->UseFollowUpScreen(FollowUpScreen)  
Loading[/Loading/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
Loading[/Loading/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
Loading[/Loading/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedBucket
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->SelectedBucket[/SelectedBucket/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->SelectedBucket[/SelectedBucket/]  
SelectedBucket[/SelectedBucket/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedBucket[/SelectedBucket/]-. use .->UseExportScreen(ExportScreen)  
SelectedBucket[/SelectedBucket/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## vContinue
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vContinue[/vContinue/]  
vContinue[/vContinue/]-. use .->Use2201_2(2201_2)  
:::
## SelectedSection
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->SelectedSection[/SelectedSection/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->SelectedSection[/SelectedSection/]  
SelectedSection[/SelectedSection/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedSection[/SelectedSection/]-. use .->UseExportScreen(ExportScreen)  
SelectedSection[/SelectedSection/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varSelectedPL
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varSelectedPL[/varSelectedPL/]  
varSelectedPL[/varSelectedPL/]-. use .->Use2201_2(2201_2)  
:::
## varDuplicatePopup
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varDuplicatePopup[/varDuplicatePopup/]  
varDuplicatePopup[/varDuplicatePopup/]-. use .->Use2201_2(2201_2)  
:::
## ShowTakenImage
  
:::mermaid  
graph LR  
SetCameraScreen(CameraScreen)-- set -->ShowTakenImage[/ShowTakenImage/]  
ShowTakenImage[/ShowTakenImage/]-. use .->UseCameraScreen(CameraScreen)  
ShowTakenImage[/ShowTakenImage/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varReviewTeam
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varReviewTeam[/varReviewTeam/]  
varReviewTeam[/varReviewTeam/]-. use .->Use2201_2(2201_2)  
:::
## AttachmentDeleteConfirm
  
:::mermaid  
graph LR  
SetAttachmentsScreen(AttachmentsScreen)-- set -->AttachmentDeleteConfirm[/AttachmentDeleteConfirm/]  
AttachmentDeleteConfirm[/AttachmentDeleteConfirm/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
AttachmentDeleteConfirm[/AttachmentDeleteConfirm/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## FollowUpEnd
  
:::mermaid  
graph LR  
SetFollowUpTimesScreen(FollowUpTimesScreen)-- set -->FollowUpEnd[/FollowUpEnd/]  
FollowUpEnd[/FollowUpEnd/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
FollowUpEnd[/FollowUpEnd/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varShowSort
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varShowSort[/varShowSort/]  
:::
## ShowPlanner
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->ShowPlanner[/ShowPlanner/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->ShowPlanner[/ShowPlanner/]  
ShowPlanner[/ShowPlanner/]-. use .->UseExportScreen(ExportScreen)  
ShowPlanner[/ShowPlanner/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
ShowPlanner[/ShowPlanner/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## FollowUpConfirmed
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->FollowUpConfirmed[/FollowUpConfirmed/]  
SetHomeScreen(HomeScreen)-- set -->FollowUpConfirmed[/FollowUpConfirmed/]  
SetFollowUpTimesScreen(FollowUpTimesScreen)-- set -->FollowUpConfirmed[/FollowUpConfirmed/]  
FollowUpConfirmed[/FollowUpConfirmed/]-. use .->UseConfirmScreen(ConfirmScreen)  
FollowUpConfirmed[/FollowUpConfirmed/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varGUID211
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varGUID211[/varGUID211/]  
varGUID211[/varGUID211/]-. use .->Use2201_2(2201_2)  
:::
## vFilter
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vFilter[/vFilter/]  
vFilter[/vFilter/]-. use .->Use2201_2(2201_2)  
:::
## vIsEdit
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vIsEdit[/vIsEdit/]  
vIsEdit[/vIsEdit/]-. use .->Use2201_2(2201_2)  
:::
## ShowOverlay
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->ShowOverlay[/ShowOverlay/]  
SetAttachmentsScreen(AttachmentsScreen)-- set -->ShowOverlay[/ShowOverlay/]  
SetExportScreen(ExportScreen)-- set -->ShowOverlay[/ShowOverlay/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->ShowOverlay[/ShowOverlay/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->ShowOverlay[/ShowOverlay/]  
ShowOverlay[/ShowOverlay/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
ShowOverlay[/ShowOverlay/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
ShowOverlay[/ShowOverlay/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
ShowOverlay[/ShowOverlay/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## FollowUpStart
  
:::mermaid  
graph LR  
SetFollowUpTimesScreen(FollowUpTimesScreen)-- set -->FollowUpStart[/FollowUpStart/]  
FollowUpStart[/FollowUpStart/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
FollowUpStart[/FollowUpStart/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedUser
  
:::mermaid  
graph LR  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->SelectedUser[/SelectedUser/]  
SelectedUser[/SelectedUser/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
SelectedUser[/SelectedUser/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varAddMemo
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varAddMemo[/varAddMemo/]  
varAddMemo[/varAddMemo/]-. use .->Use2201_2(2201_2)  
:::
## EmailConfirmed
  
:::mermaid  
graph LR  
SetWelcomeScreen(WelcomeScreen)-- set -->EmailConfirmed[/EmailConfirmed/]  
SetHomeScreen(HomeScreen)-- set -->EmailConfirmed[/EmailConfirmed/]  
SetEmailScreen(EmailScreen)-- set -->EmailConfirmed[/EmailConfirmed/]  
EmailConfirmed[/EmailConfirmed/]-. use .->UseConfirmScreen(ConfirmScreen)  
EmailConfirmed[/EmailConfirmed/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## varAddGoal
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varAddGoal[/varAddGoal/]  
:::
## ShowImageSaved
  
:::mermaid  
graph LR  
SetCameraScreen(CameraScreen)-- set -->ShowImageSaved[/ShowImageSaved/]  
ShowImageSaved[/ShowImageSaved/]-. use .->UseCameraScreen(CameraScreen)  
ShowImageSaved[/ShowImageSaved/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedPlan
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->SelectedPlan[/SelectedPlan/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->SelectedPlan[/SelectedPlan/]  
SelectedPlan[/SelectedPlan/]-. use .->UseConfirmScreen(ConfirmScreen)  
SelectedPlan[/SelectedPlan/]-. use .->UseExportScreen(ExportScreen)  
SelectedPlan[/SelectedPlan/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## UserSelectedFromTasks
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->UserSelectedFromTasks[/UserSelectedFromTasks/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->UserSelectedFromTasks[/UserSelectedFromTasks/]  
UserSelectedFromTasks[/UserSelectedFromTasks/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
UserSelectedFromTasks[/UserSelectedFromTasks/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## vShowFilter
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vShowFilter[/vShowFilter/]  
:::
## SecondsRemain
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->SecondsRemain[/SecondsRemain/]  
SecondsRemain[/SecondsRemain/]-. use .->UseHomeScreen(HomeScreen)  
SecondsRemain[/SecondsRemain/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## UserSelected
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->UserSelected[/UserSelected/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->UserSelected[/UserSelected/]  
UserSelected[/UserSelected/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
UserSelected[/UserSelected/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## SelectedUserTasks
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->SelectedUserTasks[/SelectedUserTasks/]  
SelectedUserTasks[/SelectedUserTasks/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
SelectedUserTasks[/SelectedUserTasks/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## myedit
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->myedit[/myedit/]  
:::
## ShowOneNote
  
:::mermaid  
graph LR  
SetExportScreen(ExportScreen)-- set -->ShowOneNote[/ShowOneNote/]  
SetExportPopUpsScreen(ExportPopUpsScreen)-- set -->ShowOneNote[/ShowOneNote/]  
ShowOneNote[/ShowOneNote/]-. use .->UseExportScreen(ExportScreen)  
ShowOneNote[/ShowOneNote/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
ShowOneNote[/ShowOneNote/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
##  varLoadingPopup
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->varLoadingPopup[/ varLoadingPopup/]  
:::
## vGUID221
  
:::mermaid  
graph LR  
Set2201_2(2201_2)-- set -->vGUID221[/vGUID221/]  
:::
## TaskSelected
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->TaskSelected[/TaskSelected/]  
SetHomePopUpsScreen(HomePopUpsScreen)-- set -->TaskSelected[/TaskSelected/]  
TaskSelected[/TaskSelected/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
TaskSelected[/TaskSelected/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
TaskSelected[/TaskSelected/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
:::
## MultiRecipients
  
:::mermaid  
graph LR  
SetHomeScreen(HomeScreen)-- set -->MultiRecipients[/MultiRecipients/]  
MultiRecipients[/MultiRecipients/]-. use .->UseEmailScreen(EmailScreen)  
MultiRecipients[/MultiRecipients/]-. use .->UseExportScreen(ExportScreen)  
MultiRecipients[/MultiRecipients/]-. use .->UseFollowUpScreen(FollowUpScreen)  
MultiRecipients[/MultiRecipients/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## ShowSketchSaved
  
:::mermaid  
graph LR  
SetSketchScreen(Sketch Screen)-- set -->ShowSketchSaved[/ShowSketchSaved/]  
ShowSketchSaved[/ShowSketchSaved/]-. use .->UseSketchScreen(Sketch Screen)  
ShowSketchSaved[/ShowSketchSaved/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
# Global Collects
  
Usage of global collects is shown based on the screen(s) where this collect is set, used or cleared
## Tasks
  
:::mermaid  
graph LR  
CollectHomePopUpsScreen(HomePopUpsScreen)-- collect -->Tasks[/Tasks/]  
Tasks[/Tasks/]-. use .->Use2201_2(2201_2)  
Tasks[/Tasks/]-. use .->UseWelcomeScreen(WelcomeScreen)  
Tasks[/Tasks/]-. use .->UseHomeScreen(HomeScreen)  
Tasks[/Tasks/]-. use .->UseConfirmScreen(ConfirmScreen)  
Tasks[/Tasks/]-. use .->UseExportScreen(ExportScreen)  
Tasks[/Tasks/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
Tasks[/Tasks/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## MeetingDurations
  
:::mermaid  
graph LR  
MeetingDurations[/MeetingDurations/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
MeetingDurations[/MeetingDurations/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
MeetingDurations[/MeetingDurations/]-. clear .->ClearFollowUpTimesScreen(FollowUpTimesScreen)  
:::
## MeetingTimes
  
:::mermaid  
graph LR  
MeetingTimes[/MeetingTimes/]-. use .->UseWelcomeScreen(WelcomeScreen)  
MeetingTimes[/MeetingTimes/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
MeetingTimes[/MeetingTimes/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
MeetingTimes[/MeetingTimes/]-. clear .->ClearFollowUpTimesScreen(FollowUpTimesScreen)  
:::
## colQuestionRow
  
:::mermaid  
graph LR  
colQuestionRow[/colQuestionRow/]-. use .->Use2201_2(2201_2)  
colQuestionRow[/colQuestionRow/]-. clear .->Clear2201_2(2201_2)  
:::
## TempView_Plan
  
:::mermaid  
graph LR  
TempView_Plan[/TempView_Plan/]-. use .->Use2201_2(2201_2)  
TempView_Plan[/TempView_Plan/]-. clear .->Clear2201_2(2201_2)  
:::
## TempRi_Question
  
:::mermaid  
graph LR  
TempRi_Question[/TempRi_Question/]-. use .->Use2201_2(2201_2)  
TempRi_Question[/TempRi_Question/]-. clear .->Clear2201_2(2201_2)  
:::
## TempPl_Allocation
  
:::mermaid  
graph LR  
TempPl_Allocation[/TempPl_Allocation/]-. use .->Use2201_2(2201_2)  
TempPl_Allocation[/TempPl_Allocation/]-. clear .->Clear2201_2(2201_2)  
:::
## FollowUpMeetingAttendees
  
:::mermaid  
graph LR  
CollectFollowUpScreen(FollowUpScreen)-- collect -->FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]  
FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]-. use .->UseWelcomeScreen(WelcomeScreen)  
FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]-. use .->UseFollowUpScreen(FollowUpScreen)  
FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
FollowUpMeetingAttendees[/FollowUpMeetingAttendees/]-. clear .->ClearFollowUpScreen(FollowUpScreen)  
:::
## OneNoteBooks
  
:::mermaid  
graph LR  
OneNoteBooks[/OneNoteBooks/]-. use .->UseExportScreen(ExportScreen)  
OneNoteBooks[/OneNoteBooks/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
OneNoteBooks[/OneNoteBooks/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
OneNoteBooks[/OneNoteBooks/]-. clear .->ClearExportScreen(ExportScreen)  
:::
## colPlDistribution
  
:::mermaid  
graph LR  
colPlDistribution[/colPlDistribution/]-. clear .->Clear2201_2(2201_2)  
:::
## colDetailRow
  
:::mermaid  
graph LR  
colDetailRow[/colDetailRow/]-. use .->Use2201_2(2201_2)  
colDetailRow[/colDetailRow/]-. clear .->Clear2201_2(2201_2)  
:::
## Sketches
  
:::mermaid  
graph LR  
CollectSketchScreen(Sketch Screen)-- collect -->Sketches[/Sketches/]  
Sketches[/Sketches/]-. use .->UseWelcomeScreen(WelcomeScreen)  
Sketches[/Sketches/]-. use .->UseHomeScreen(HomeScreen)  
Sketches[/Sketches/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
Sketches[/Sketches/]-. use .->UseConfirmScreen(ConfirmScreen)  
Sketches[/Sketches/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## MeetingAttendeesTemp
  
:::mermaid  
graph LR  
MeetingAttendeesTemp[/MeetingAttendeesTemp/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
MeetingAttendeesTemp[/MeetingAttendeesTemp/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
MeetingAttendeesTemp[/MeetingAttendeesTemp/]-. clear .->ClearHomePopUpsScreen(HomePopUpsScreen)  
:::
## colAnswerRow
  
:::mermaid  
graph LR  
colAnswerRow[/colAnswerRow/]-. clear .->Clear2201_2(2201_2)  
:::
## TemplateData
  
:::mermaid  
graph LR  
TemplateData[/TemplateData/]-. use .->UseConfirmScreen(ConfirmScreen)  
TemplateData[/TemplateData/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
TemplateData[/TemplateData/]-. clear .->ClearConfirmScreen(ConfirmScreen)  
:::
## colPlAssignment
  
:::mermaid  
graph LR  
colPlAssignment[/colPlAssignment/]-. use .->Use2201_2(2201_2)  
colPlAssignment[/colPlAssignment/]-. clear .->Clear2201_2(2201_2)  
:::
## Templates
  
:::mermaid  
graph LR  
Templates[/Templates/]-. use .->UseConfirmScreen(ConfirmScreen)  
Templates[/Templates/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
Templates[/Templates/]-. clear .->ClearWelcomeScreen(WelcomeScreen)  
:::
## colAdTraegerCurrent
  
:::mermaid  
graph LR  
colAdTraegerCurrent[/colAdTraegerCurrent/]-. clear .->Clear2201_2(2201_2)  
:::
## colAdAssignment
  
:::mermaid  
graph LR  
colAdAssignment[/colAdAssignment/]-. clear .->Clear2201_2(2201_2)  
:::
## TempAu_Level_4
  
:::mermaid  
graph LR  
TempAu_Level_4[/TempAu_Level_4/]-. clear .->Clear2201_2(2201_2)  
:::
## colQuestionsAdd
  
:::mermaid  
graph LR  
colQuestionsAdd[/colQuestionsAdd/]-. use .->Use2201_2(2201_2)  
colQuestionsAdd[/colQuestionsAdd/]-. clear .->Clear2201_2(2201_2)  
:::
## colAllocation
  
:::mermaid  
graph LR  
colAllocation[/colAllocation/]-. clear .->Clear2201_2(2201_2)  
:::
## HoursList
  
:::mermaid  
graph LR  
HoursList[/HoursList/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
HoursList[/HoursList/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
HoursList[/HoursList/]-. clear .->ClearFollowUpTimesScreen(FollowUpTimesScreen)  
:::
## TempRisk
  
:::mermaid  
graph LR  
TempRisk[/TempRisk/]-. use .->Use2201_2(2201_2)  
TempRisk[/TempRisk/]-. clear .->Clear2201_2(2201_2)  
:::
## EmailAttachments
  
:::mermaid  
graph LR  
CollectConfirmScreen(ConfirmScreen)-- collect -->EmailAttachments[/EmailAttachments/]  
EmailAttachments[/EmailAttachments/]-. use .->UseWelcomeScreen(WelcomeScreen)  
EmailAttachments[/EmailAttachments/]-. use .->UseConfirmScreen(ConfirmScreen)  
EmailAttachments[/EmailAttachments/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## PlannerBuckets
  
:::mermaid  
graph LR  
PlannerBuckets[/PlannerBuckets/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
PlannerBuckets[/PlannerBuckets/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
PlannerBuckets[/PlannerBuckets/]-. clear .->ClearExportScreen(ExportScreen)  
PlannerBuckets[/PlannerBuckets/]-. clear .->ClearExportPopUpsScreen(ExportPopUpsScreen)  
:::
## colFlowResponse
  
:::mermaid  
graph LR  
colFlowResponse[/colFlowResponse/]-. use .->Use2201_2(2201_2)  
colFlowResponse[/colFlowResponse/]-. clear .->Clear2201_2(2201_2)  
:::
## colPlDistributionCurrent
  
:::mermaid  
graph LR  
colPlDistributionCurrent[/colPlDistributionCurrent/]-. clear .->Clear2201_2(2201_2)  
:::
## MeetingAttendeeEmails
  
:::mermaid  
graph LR  
MeetingAttendeeEmails[/MeetingAttendeeEmails/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
MeetingAttendeeEmails[/MeetingAttendeeEmails/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
MeetingAttendeeEmails[/MeetingAttendeeEmails/]-. clear .->ClearHomePopUpsScreen(HomePopUpsScreen)  
:::
## Photos
  
:::mermaid  
graph LR  
CollectCameraScreen(CameraScreen)-- collect -->Photos[/Photos/]  
Photos[/Photos/]-. use .->UseWelcomeScreen(WelcomeScreen)  
Photos[/Photos/]-. use .->UseHomeScreen(HomeScreen)  
Photos[/Photos/]-. use .->UseSketchScreen(Sketch Screen)  
Photos[/Photos/]-. use .->UseCameraScreen(CameraScreen)  
Photos[/Photos/]-. use .->UseAttachmentsScreen(AttachmentsScreen)  
Photos[/Photos/]-. use .->UseConfirmScreen(ConfirmScreen)  
Photos[/Photos/]-. use .->UseExportScreen(ExportScreen)  
Photos[/Photos/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## TempAu_Level_3
  
:::mermaid  
graph LR  
TempAu_Level_3[/TempAu_Level_3/]-. clear .->Clear2201_2(2201_2)  
:::
## PlannerPlans
  
:::mermaid  
graph LR  
PlannerPlans[/PlannerPlans/]-. use .->UseExportScreen(ExportScreen)  
PlannerPlans[/PlannerPlans/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
PlannerPlans[/PlannerPlans/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
PlannerPlans[/PlannerPlans/]-. clear .->ClearExportScreen(ExportScreen)  
:::
## updateTable2201auGoals
  
:::mermaid  
graph LR  
updateTable2201auGoals[/updateTable2201auGoals/]-. use .->Use2201_2(2201_2)  
updateTable2201auGoals[/updateTable2201auGoals/]-. clear .->Clear2201_2(2201_2)  
:::
## patchTable2011riDetail
  
:::mermaid  
graph LR  
Collect2201_2(2201_2)-- collect -->patchTable2011riDetail[/patchTable2011riDetail/]  
patchTable2011riDetail[/patchTable2011riDetail/]-. use .->Use2201_2(2201_2)  
:::
## TempPl_Goals
  
:::mermaid  
graph LR  
TempPl_Goals[/TempPl_Goals/]-. use .->Use2201_2(2201_2)  
TempPl_Goals[/TempPl_Goals/]-. clear .->Clear2201_2(2201_2)  
:::
## MeetingAttendees
  
:::mermaid  
graph LR  
MeetingAttendees[/MeetingAttendees/]-. use .->UseWelcomeScreen(WelcomeScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseHomeScreen(HomeScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseConfirmScreen(ConfirmScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseFollowUpScreen(FollowUpScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseFollowUpTimesScreen(FollowUpTimesScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseHomePopUpsScreen(HomePopUpsScreen)  
MeetingAttendees[/MeetingAttendees/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
MeetingAttendees[/MeetingAttendees/]-. clear .->ClearHomePopUpsScreen(HomePopUpsScreen)  
:::
## Indexes
  
:::mermaid  
graph LR  
CollectConfirmScreen(ConfirmScreen)-- collect -->Indexes[/Indexes/]  
Indexes[/Indexes/]-. use .->UseConfirmScreen(ConfirmScreen)  
Indexes[/Indexes/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
:::
## OneNoteSections
  
:::mermaid  
graph LR  
OneNoteSections[/OneNoteSections/]-. use .->UseExportPopUpsScreen(ExportPopUpsScreen)  
OneNoteSections[/OneNoteSections/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
OneNoteSections[/OneNoteSections/]-. clear .->ClearExportScreen(ExportScreen)  
OneNoteSections[/OneNoteSections/]-. clear .->ClearExportPopUpsScreen(ExportPopUpsScreen)  
:::
## colAdRolle
  
:::mermaid  
graph LR  
colAdRolle[/colAdRolle/]-. clear .->Clear2201_2(2201_2)  
:::
## colModelRow
  
:::mermaid  
graph LR  
colModelRow[/colModelRow/]-. use .->Use2201_2(2201_2)  
colModelRow[/colModelRow/]-. clear .->Clear2201_2(2201_2)  
:::
## colAdTraeger
  
:::mermaid  
graph LR  
colAdTraeger[/colAdTraeger/]-. use .->Use2201_2(2201_2)  
colAdTraeger[/colAdTraeger/]-. clear .->Clear2201_2(2201_2)  
:::
## EmailRecipients
  
:::mermaid  
graph LR  
CollectExportScreen(ExportScreen)-- collect -->EmailRecipients[/EmailRecipients/]  
EmailRecipients[/EmailRecipients/]-. use .->UseWelcomeScreen(WelcomeScreen)  
EmailRecipients[/EmailRecipients/]-. use .->UseEmailScreen(EmailScreen)  
EmailRecipients[/EmailRecipients/]-. use .->UseConfirmScreen(ConfirmScreen)  
EmailRecipients[/EmailRecipients/]-. use .->UseExportScreen(ExportScreen)  
EmailRecipients[/EmailRecipients/]-. use .->UseCollectionsAndVariables(CollectionsAndVariables)  
EmailRecipients[/EmailRecipients/]-. clear .->ClearHomeScreen(HomeScreen)  
EmailRecipients[/EmailRecipients/]-. clear .->ClearExportScreen(ExportScreen)  
:::
# Global Flows
  
Usage of global flows is shown based on the screen(s) where this flows is executed. 
## weDit_SQL_runOperations
  
:::mermaid  
graph LR  
weDit_SQL_runOperations[/weDit_SQL_runOperations/]-. executed_from .->executed_from2201_2(2201_2)  
:::
## weDit_SQL_modRiskAssessment
  
:::mermaid  
graph LR  
weDit_SQL_modRiskAssessment[/weDit_SQL_modRiskAssessment/]-. executed_from .->executed_from2201_2(2201_2)  
:::