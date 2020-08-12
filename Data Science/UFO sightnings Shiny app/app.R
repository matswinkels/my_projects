# UFO sightings data exploration Shiny App

library(shiny)
library(ggplot2)
library(dplyr)

# preparing data
UFO <- read.csv("usaUFOsightings.csv", header = TRUE, stringsAsFactors = FALSE)
UFO$date_sighted = as.Date(UFO$date_sighted)
states <- as.vector(unique(UFO$state))

ui <- fluidPage(
    theme = shinythemes::shinytheme('yeti'),
    titlePanel('UFO sightings'),
    sidebarLayout(
        sidebarPanel(
            selectInput('state',
                        'Select U.S. state',
                        selected = 'AK',
                        choices = states),
            dateRangeInput('date_sighted',
                           'Select a date range',
                           start = min(UFO$date_sighted),
                           end = max(UFO$date_sighted),
                           min = min(UFO$date_sighted),
                           max = max(UFO$date_sighted),
                           format = "yyyy-mm-dd",
                           separator = "to")),
        mainPanel(
            tabsetPanel(tabPanel('Plot',
                                 plotOutput('plot')),
                        tabPanel('Table',
                                 DT::DTOutput('table'))))))
server <- function(input, output, session){
    output$plot <- renderPlot(
        {UFO %>%
                filter(state == input$state, date_sighted >= input$date_sighted[1], date_sighted <= input$date_sighted[2]) %>%
                ggplot(UFO, mapping = aes(factor(shape))) +
                geom_bar(stat="count", position = "dodge") +
                labs(x = "Shape",
                     y = "#Sighted") +
                theme(axis.text.x = element_text(angle=90, size=15, vjust=0.3),
                      axis.title.x = element_text(size=20),
                      axis.title.y = element_text(size=20))
        })
    
    output$table <- DT::renderDT(
        {UFO %>%
                filter(state == input$state) %>%
                filter(date_sighted >= input$date_sighted[1], date_sighted <= input$date_sighted[2]) %>%
                group_by(shape) %>%
                summarise_at(vars(duration_sec),
                             list(~n(), ~mean(.), ~median(.), ~min(.), ~max(.))) %>%
                DT::datatable()}
    )
}

shinyApp(ui = ui, server = server)
