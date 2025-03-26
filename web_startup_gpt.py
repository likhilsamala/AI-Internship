from flask import Flask, render_template, request, jsonify
import os
from typing import Dict

# Simulate the AI SDK imports (in a real implementation, you would import from the actual AI SDK)
def simulate_ai_sdk():
    class GenerateText:
        def __call__(self, options):
            # Simulate the generateText function
            model = options.get('model', None)
            prompt = options.get('prompt', '')
            system = options.get('system', '')
            
            # In a real implementation, this would call the actual AI model
            response = ""
            if "investor" in prompt.lower():
                response = """Based on your industry focus, here are some potential investors:

Venture Capital Firms:
1. Industry Ventures - Typically invests $1-5M in early-stage startups
2. Innovation Capital - Has a portfolio of 15+ companies with average investment of $3M

Angel Investors:
1. Sarah Johnson - Former executive with 10+ investments in the sector
2. Michael Chen - Technical background with interest in innovations

Crowdfunding Platforms:
1. SectorStart - Specializes in startups with average raise of $250K
2. FundLaunch - General platform with successful campaigns"""
            elif "pitch deck" in prompt.lower():
                response = """Here are suggestions to improve your pitch deck:

Problem Statement:
- Quantify the problem with specific market data
- Include 1-2 customer testimonials describing the pain point
- Use visual representation of the problem's impact

Solution:
- Clearly explain how your solution addresses each aspect of the problem
- Include a product demo or screenshots
- Highlight your unique value proposition with competitive advantages"""
            elif "fundraising strategy" in prompt.lower():
                response = """Step-by-Step Fundraising Strategy:

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
   - Complete due diligence and close the round"""
            elif "digital marketing" in prompt.lower():
                response = """Digital Marketing Strategies for Early-Stage Startups:

1. Social Media Marketing:
   - Focus on 1-2 platforms where your target audience is most active
   - Create a content calendar with 2-3 weekly posts
   - Allocate 15-20% of marketing budget for paid social campaigns

2. Content Marketing:
   - Develop thought leadership content addressing customer pain points
   - Create a company blog with weekly posts on industry trends
   - Repurpose content across multiple channels"""
            else:
                response = "I can help with fundraising, pitch decks, and digital marketing strategies. Please ask a specific question about these topics."
            
            return {"text": response, "finishReason": "stop", "usage": {"promptTokens": 100, "completionTokens": 150}}
    
    class OpenAI:
        def __call__(self, model_name):
            return f"openai-{model_name}"
    
    return GenerateText(), OpenAI()

# Simulate the AI SDK imports
generateText, openai = simulate_ai_sdk()

app = Flask(__name__)

class StartupGPT:
    def __init__(self):
        self.model = openai('gpt-4o')  # In a real implementation, this would be the actual model
        self.welcome_message = """Welcome to Startup GPT! 🚀 Whether you're seeking fundraising advice, refining your pitch deck, or exploring growth strategies, we're here to help. Ask your questions, and let's build your startup's success story together."""
        self.example_prompts = [
            "I'm a startup founder in the fintech sector, and I'm looking for potential investors. Can you suggest suitable venture capitalists, angel investors, or crowdfunding platforms that specialize in my industry?",
            "I've created a pitch deck for my startup that focuses on a SaaS platform for remote teams. Can you review my key slides and suggest improvements?",
            "I'm preparing to raise a seed round for my startup. Can you help me build a step-by-step fundraising strategy?",
            "Can you explain digital marketing strategies for early-stage startups?"
        ]
        
        # System prompts for different query types
        self.system_prompts = {
            "investor": "You are an expert in venture capital and startup fundraising. Provide specific, actionable advice about investors for startup founders.",
            "pitch_deck": "You are a pitch deck expert who has helped startups raise millions in funding. Provide specific, actionable advice for improving pitch decks.",
            "strategy": "You are a fundraising strategist with experience in helping startups raise capital. Provide specific, actionable fundraising strategies.",
            "marketing": "You are a digital marketing expert specializing in startup growth. Provide specific, actionable marketing strategies for early-stage startups."
        }
    
    def get_system_prompt(self, user_query: str) -> str:
        """Determine the appropriate system prompt based on the user query"""
        if "investor" in user_query.lower():
            return self.system_prompts["investor"]
        elif "pitch deck" in user_query.lower():
            return self.system_prompts["pitch_deck"]
        elif "fundraising strategy" in user_query.lower():
            return self.system_prompts["strategy"]
        elif "digital marketing" in user_query.lower():
            return self.system_prompts["marketing"]
        else:
            # Default system prompt
            return "You are Startup GPT, an AI assistant specialized in helping startup founders with fundraising, pitch decks, and growth strategies. Provide specific, actionable advice."
    
    def generate_response(self, user_query: str) -> str:
        """Generate a response using the AI SDK"""
        system_prompt = self.get_system_prompt(user_query)
        
        # In a real implementation, this would be an actual API call
        response = generateText({
            'model': self.model,
            'prompt': user_query,
            'system': system_prompt
        })
        
        return response["text"]

# Create an instance of the chatbot
chatbot = StartupGPT()

@app.route('/')
def home():
    # In a real implementation, you would have an HTML template
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Startup GPT</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            .chat-container {{
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 20px;
                height: 400px;
                overflow-y: auto;
                margin-bottom: 20px;
            }}
            .message {{
                margin-bottom: 15px;
                padding: 10px;
                border-radius: 5px;
            }}
            .user-message {{
                background-color: #e6f7ff;
                text-align: right;
            }}
            .bot-message {{
                background-color: #f0f0f0;
            }}
            .input-container {{
                display: flex;
            }}
            #user-input {{
                flex-grow: 1;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}
            button {{
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                margin-left: 10px;
                cursor: pointer;
            }}
            .example-prompts {{
                margin-top: 20px;
            }}
            .example-prompt {{
                cursor: pointer;
                color: #0066cc;
                margin-bottom: 5px;
            }}
        </style>
    </head>
    <body>
        <h1>Startup GPT</h1>
        <div class="chat-container" id="chat-container">
            <div class="message bot-message">{chatbot.welcome_message}</div>
        </div>
        <div class="input-container">
            <input type="text" id="user-input" placeholder="Type your question here...">
            <button onclick="sendMessage()">Send</button>
        </div>
        <div class="example-prompts">
            <h3>Example prompts:</h3>
            <div class="example-prompt" onclick="useExamplePrompt(this.innerText)">
                {chatbot.example_prompts[0]}
            </div>
            <div class="example-prompt" onclick="useExamplePrompt(this.innerText)">
                {chatbot.example_prompts[1]}
            </div>
            <div class="example-prompt" onclick="useExamplePrompt(this.innerText)">
                {chatbot.example_prompts[2]}
            </div>
            <div class="example-prompt" onclick="useExamplePrompt(this.innerText)">
                {chatbot.example_prompts[3]}
            </div>
        </div>

        <script>
            function sendMessage() {{
                const userInput = document.getElementById('user-input').value;
                if (userInput.trim() === '') return;
                
                // Add user message to chat
                const chatContainer = document.getElementById('chat-container');
                const userMessageDiv = document.createElement('div');
                userMessageDiv.className = 'message user-message';
                userMessageDiv.innerText = userInput;
                chatContainer.appendChild(userMessageDiv);
                
                // Clear input
                document.getElementById('user-input').value = '';
                
                // Send request to server
                fetch('/get_response', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                    }},
                    body: JSON.stringify({{ query: userInput }}),
                }})
                .then(response => response.json())
                .then(data => {{
                    // Add bot response to chat
                    const botMessageDiv = document.createElement('div');
                    botMessageDiv.className = 'message bot-message';
                    botMessageDiv.innerText = data.response;
                    chatContainer.appendChild(botMessageDiv);
                    
                    // Scroll to bottom
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }})
                .catch(error => {{
                    console.error('Error:', error);
                }});
                
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }}
            
            function useExamplePrompt(prompt) {{
                document.getElementById('user-input').value = prompt;
            }}
            
            // Allow Enter key to send message
            document.getElementById('user-input').addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') {{
                    sendMessage();
                }}
            }});
        </script>
    </body>
    </html>
    """
    return html

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    user_query = data.get('query', '')
    response = chatbot.generate_response(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    # In a real implementation, you would set the host and port appropriately
    app.run(debug=True)