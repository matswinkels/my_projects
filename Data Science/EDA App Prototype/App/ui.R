library(shiny)
library(PogromcyDanych)
library(readxl)
library(shinyWidgets)

# read_excel('C:/Users/mrswi/Desktop/Powiaty Analiza/Powiaty.xlsx', 
#            col_names=TRUE) -> PowiatyData
# PowiatyData <- as_tibble(subset(PowiatyData, select = -c(IdTer)))
# PowiatyData$Wojewodztwo <- as.factor(PowiatyData$Wojewodztwo)
# PowiatyData$PowiatMiasto <- as.factor(PowiatyData$PowiatMiasto)
# PowiatyData$Makroregion <- as.factor(PowiatyData$Makroregion)
# 
# voiv_list <- unique(as.character(PowiatyData$Wojewodztwo))


cuts_list <- unique(as.character(diamonds$cut))
color_list <- unique(as.character(diamonds$color))
clarity_list <- unique(as.character(diamonds$clarity))

shinyUI(fluidPage(theme = shinythemes::shinytheme('yeti'),
                  
    titlePanel("Data Exploration App"),
    navbarPage(title = 'Menu',
               tabPanel(icon("home")),
               
               tabPanel('Dataset',
                        fluidRow(
                            column(
                                h3('You can explore dataset presented in a data frame, shown below. Use filters to specify your needs.'), width=8),
                            
                            column(width=4)
                        ),
                        
                        sidebarLayout(
                            sidebarPanel(
                                pickerInput('PickCut',
                                            label = 'Choose cuts:',
                                            selected = cuts_list,
                                            choices = cuts_list,
                                            options = list(`actions-box` = TRUE),
                                            multiple = T),
                                pickerInput('PickClarity',
                                            label = 'Choose clarity:',
                                            selected = clarity_list,
                                            choices = clarity_list,
                                            options = list(`actions-box` = TRUE),
                                            multiple = T),
                                pickerInput('PickColor',
                                            label = 'Choose color:',
                                            selected = color_list,
                                            choices = color_list,
                                            options = list(`actions-box` = TRUE),
                                            multiple = T)
                            ),
                            mainPanel(DT::DTOutput('data_table'))
                        )),
               
               tabPanel('Plots',
                        sidebarLayout(
                            sidebarPanel(
                                selectInput('InCut',
                                            label = 'Choose cut:',
                                            selected = 'Fair',
                                            choices = cuts_list)
                            ),
                            mainPanel(
                                tabsetPanel(tabPanel('Histogram', plotOutput('hist')),
                                            tabPanel('Scatter plot', plotOutput('scatter')))
                            )
                        )),
               tabPanel('Plots 2',
                        tabsetPanel(tabPanel('Histogram',
                                             sidebarLayout(
                                               sidebarPanel(
                                                 selectInput('InCut2',
                                                             label = 'Choose cut:',
                                                             selected = 'Fair',
                                                             choices = cuts_list)
                                               ),
                                               mainPanel(
                                                 plotOutput('hist2')
                                               )
                                             )),
                                    tabPanel('Scatter',
                                             sidebarLayout(
                                               sidebarPanel(
                                                 selectInput('InCut3',
                                                             label = 'Choose cut:',
                                                             selected = 'Fair',
                                                             choices = cuts_list)
                                               ),
                                               mainPanel(
                                                 plotOutput('scatter2')
                                               )
                                             ))

                        )),
               tabPanel(icon('info')))))
