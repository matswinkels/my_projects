library(shiny)
library(dplyr)
library(ggplot2)
library(ggthemes)

shinyServer(function(input, output) {
    output$hist <- renderPlot(
        {
            diamonds %>% 
                filter(cut == input$InCut) %>% 
                ggplot(aes(x = depth)) +
                geom_histogram(color = 'white') +
                theme_solarized()
        }
    )
    
    output$hist2 <- renderPlot(
        {
            diamonds %>% 
                filter(cut == input$InCut2) %>% 
                ggplot(aes(x = depth)) +
                geom_histogram(color = 'white') +
                theme_solarized()
        }
    )
    
    
    # observe({
    #     print(input$PickCut)
    # })
    
    output$data_table <- DT::renderDT(
        {
            validate(need(input$PickCut, "No data fits your filters."))
            validate(need(input$PickClarity, "No data fits your filters."))
            validate(need(input$PickColor, "No data fits your filters."))
            diamonds %>% 
                filter(cut == input$PickCut) %>% 
                filter(clarity == input$PickClarity) %>% 
                filter(color == input$PickColor)
        }
    )
    
    output$scatter <- renderPlot(
        {
            diamonds %>% 
                filter(cut == input$InCut) %>% 
                ggplot(aes(x = depth, y = price)) +
                geom_point(aes(color = color)) +
                theme_solarized()
        }
    )
    
    output$scatter2 <- renderPlot(
        {
            diamonds %>% 
                filter(cut == input$InCut3) %>% 
                ggplot(aes(x = depth, y = price)) +
                geom_point(aes(color = color)) +
                theme_solarized()
        }
    )
    
    

})
