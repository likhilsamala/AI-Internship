def display_header(title):
    """Display a formatted header"""
    print("\n" + "=" * 80)
    print(f"{title.center(80)}")
    print("=" * 80 + "\n")

def task1_fundraising_prompts():
    """Task 1: Create three unique prompts for a chatbot to assist with fundraising strategies"""
    display_header("TASK 1: FUNDRAISING PROMPTS")
    
    prompts = [
        {
            "title": "Investor Identification",
            "prompt": "I'm a startup founder in the [industry name] sector, and I'm looking for potential investors. Can you suggest suitable venture capitalists, angel investors, or crowdfunding platforms that specialize in my industry? Please provide details on their investment preferences and previous investments.",
            "explanation": "This prompt helps founders find relevant investors by specifying their industry and the type of investment they are seeking. The chatbot can provide tailored recommendations."
        },
        {
            "title": "Pitch Deck Improvement",
            "prompt": "I've created a pitch deck for my startup that focuses on [brief description of product/service]. Can you review my key slides (problem statement, solution, market analysis, and financials) and suggest improvements to make it more persuasive for potential investors?",
            "explanation": "This prompt is useful for founders looking to strengthen their pitch decks. By requesting feedback on specific sections, they can refine their presentations to attract investors."
        },
        {
            "title": "Fundraising Strategy Development",
            "prompt": "I'm preparing to raise a [seed/Series A/B] round for my startup. Can you help me build a step-by-step fundraising strategy? Please include recommendations on timelines, types of investors to approach, and essential metrics to showcase.",
            "explanation": "This prompt enables founders to receive a structured plan for their fundraising efforts. It ensures they are aware of key milestones, investor types, and financial metrics."
        }
    ]
    
    for i, prompt_data in enumerate(prompts, 1):
        print(f"Prompt {i}: {prompt_data['title']}")
        print(f"Text: \"{prompt_data['prompt']}\"")
        print(f"Explanation: {prompt_data['explanation']}")
        print("\n" + "-" * 80 + "\n")
    
    return prompts

def task2_improved_prompt():
    """Task 2: Improve a basic prompt about digital marketing"""
    display_header("TASK 2: IMPROVED DIGITAL MARKETING PROMPT")
    
    original_prompt = "Tell me about digital marketing."
    improved_prompt = "Can you explain digital marketing strategies for early-stage startups? Please cover essential channels like social media marketing, content marketing, email campaigns, and SEO. Additionally, include tips on budget allocation and measuring ROI."
    
    explanation = """
The improved prompt makes the request more specific by:
1. Defining the target audience (early-stage startups)
2. Specifying the desired information (digital marketing strategies)
3. Breaking down the query into clear subtopics (channels, budget, ROI)
4. Ensuring the chatbot can provide a detailed and actionable response
"""
    
    print(f"Original Prompt: \"{original_prompt}\"")
    print(f"Improved Prompt: \"{improved_prompt}\"")
    print(f"Explanation: {explanation}")
    
    return {
        "original": original_prompt,
        "improved": improved_prompt,
        "explanation": explanation
    }

def task3_welcome_message():
    """Task 3: Create a welcome message for a Startup GPT chatbot"""
    display_header("TASK 3: STARTUP GPT WELCOME MESSAGE")
    
    welcome_message = """Welcome to Startup GPT! 🚀 Whether you're seeking fundraising advice, refining your pitch deck, or exploring growth strategies, we're here to help. Ask your questions, and let's build your startup's success story together. Ready to get started?"""
    
    explanation = """
This welcome message:
1. Sets a positive and engaging tone with enthusiastic language and emojis
2. Clearly outlines the chatbot's primary functions (fundraising, pitch deck, growth strategies)
3. Encourages founders to ask relevant questions
4. Uses a conversational style to make users feel comfortable
5. Ends with a question to prompt immediate engagement
"""
    
    print(f"Welcome Message: \"{welcome_message}\"")
    print(f"Explanation: {explanation}")
    
    return {
        "message": welcome_message,
        "explanation": explanation
    }

def interactive_demo(fundraising_prompts, marketing_prompt, welcome_message):
    """Provide an interactive demo of the chatbot prompts"""
    display_header("INTERACTIVE DEMO")
    
    print(welcome_message["message"])
    print("\nThis is a simple demo of how the prompts would work in a chatbot.")
    print("You can select a prompt to see a simulated response.\n")
    
    while True:
        print("\nAvailable options:")
        print("1. Try Fundraising Prompt 1: Investor Identification")
        print("2. Try Fundraising Prompt 2: Pitch Deck Improvement")
        print("3. Try Fundraising Prompt 3: Fundraising Strategy Development")
        print("4. Try Improved Digital Marketing Prompt")
        print("5. Exit Demo")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            industry = input("Enter your industry (e.g., fintech, healthcare, edtech): ")
            prompt = fundraising_prompts[0]["prompt"].replace("[industry name]", industry)
            print(f"\nUser: {prompt}")
            print("\nStartup GPT: Based on your request for investors in the " + industry + " sector, here are some recommendations:")
            print(f"""
Venture Capital Firms:
1. {industry.title()} Ventures - Typically invests $1-5M in early-stage {industry} startups
2. Innovation Capital - Has a portfolio of 15+ {industry} companies

Angel Investors:
1. Sarah Johnson - Former {industry} executive with 10+ investments in the sector
2. Michael Chen - Technical background with interest in {industry} innovations

Crowdfunding Platforms:
1. SectorStart - Specializes in {industry} startups with average raise of $250K
2. FundLaunch - General platform with successful {industry} campaigns
            """)
            
        elif choice == "2":
            product = input("Enter a brief description of your product/service: ")
            prompt = fundraising_prompts[1]["prompt"].replace("[brief description of product/service]", product)
            print(f"\nUser: {prompt}")
            print("\nStartup GPT: Here are suggestions to improve your pitch deck for " + product + ":")
            print("""
Problem Statement:
- Quantify the problem with specific market data
- Include 1-2 customer testimonials describing the pain point
- Use visual representation of the problem's impact

Solution:
- Clearly explain how your solution addresses each aspect of the problem
- Include a product demo or screenshots
- Highlight your unique value proposition with competitive advantages

Market Analysis:
- Define your TAM, SAM, and SOM with credible sources
- Show growth trends in your specific segment
- Identify key competitors and your differentiators

Financials:
- Present clear revenue projections for 3-5 years
- Explain your business model and unit economics
- Be transparent about funding requirements and use of funds
            """)
            
        elif choice == "3":
            round_type = input("Enter your funding round (seed, Series A, Series B): ")
            prompt = fundraising_prompts[2]["prompt"].replace("[seed/Series A/B]", round_type)
            print(f"\nUser: {prompt}")
            print("\nStartup GPT: Here's a step-by-step fundraising strategy for your " + round_type + " round:")
            print(f"""
Timeline (6-month plan):
1. Months 1-2: Preparation phase
   - Finalize pitch deck and financial projections
   - Develop investor target list
   - Prepare data room with key documents

2. Months 3-4: Outreach phase
   - Begin warm introductions to investors
   - Attend industry events and pitch competitions
   - Schedule initial meetings

3. Months 5-6: Closing phase
   - Follow up with interested investors
   - Negotiate term sheets
   - Complete due diligence and close the round

Investor Types for {round_type}:
{"- Angel investors with industry expertise\n- Seed-stage focused VCs\n- Accelerators and incubators" if "seed" in round_type.lower() else "- Early-stage VCs with $50M-$200M funds\n- Corporate venture arms\n- Family offices with tech focus" if "a" in round_type.lower() else "- Growth-stage VCs with $200M+ funds\n- Private equity firms with venture arms\n- Strategic corporate investors"}

Essential Metrics to Showcase:
- User/customer growth rate (MoM or YoY)
- Revenue growth and projections
- Customer acquisition cost (CAC)
- Lifetime value (LTV)
- Burn rate and runway
- Market penetration and expansion potential
            """)
            
        elif choice == "4":
            print(f"\nUser: {marketing_prompt['improved']}")
            print("\nStartup GPT: Here are digital marketing strategies for early-stage startups:")
            print("""
1. Social Media Marketing:
   - Focus on 1-2 platforms where your target audience is most active
   - Create a content calendar with 2-3 weekly posts
   - Allocate 15-20% of marketing budget for paid social campaigns
   - Measure: Engagement rate, follower growth, click-through rates

2. Content Marketing:
   - Develop thought leadership content addressing customer pain points
   - Create a company blog with weekly posts on industry trends
   - Repurpose content across multiple channels
   - Measure: Page views, time on page, lead generation from content

3. Email Campaigns:
   - Build an email list through website sign-ups and lead magnets
   - Segment your audience for targeted messaging
   - Implement automated welcome sequences and nurture campaigns
   - Measure: Open rates, click rates, conversion rates, list growth

4. SEO Strategy:
   - Conduct keyword research focused on low-competition, high-intent terms
   - Optimize website structure and on-page elements
   - Create content around target keywords
   - Measure: Organic traffic, keyword rankings, backlink growth

Budget Allocation for Early-Stage Startups:
- 30% - Content creation and SEO
- 25% - Paid advertising (social and search)
- 20% - Email marketing tools and campaigns
- 15% - Analytics and tracking tools
- 10% - Experimental channels and testing

Measuring ROI:
- Set up proper tracking with Google Analytics and UTM parameters
- Calculate customer acquisition cost (CAC) by channel
- Track conversion rates at each funnel stage
- Implement attribution modeling to understand touchpoints
- Review and adjust strategy monthly based on performance data
            """)
            
        elif choice == "5":
            print("\nThank you for trying the Startup GPT demo!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

def main():
    """Main function to run all tasks"""
    print("STARTUP GPT CHATBOT TASKS IMPLEMENTATION")
    
    # Execute all three tasks
    fundraising_prompts = task1_fundraising_prompts()
    marketing_prompt = task2_improved_prompt()
    welcome_message = task3_welcome_message()
    
    # Run interactive demo
    interactive_demo(fundraising_prompts, marketing_prompt, welcome_message)

if __name__ == "__main__":
    main()