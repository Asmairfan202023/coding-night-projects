from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]


money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]
business_ideas = [
    "Eco-Friendly Products - Launch a business selling sustainable items.",
    "Pet Services - Grooming, walking, or training pets.",
    "Mobile Car Wash - Start a water-saving car cleaning service.",
    "Virtual Assistant - Provide administrative support remotely.",
    "Meal Prep Services - Sell healthy ready-to-eat meals.",
    "Event Planning - Organize parties, weddings, and corporate events.",
    "Digital Products - Sell eBooks, templates, or courses.",
    "Home Cleaning Services - Offer professional cleaning locally.",
    "Subscription Boxes - Curated packages for niche markets.",
    "Fitness Coaching - Online or in-person personal training.",
]

motivational_quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Push yourself, because no one else is going to do it for you.",
    "Your limitation—it’s only your imagination.",
    "Great things never come from comfort zones.",
]


@app.get("/")
def read_root():
    return {
        "message": "Welcome! Visit /side_hustles, /money_quotes, /business_ideas or /motivational_quotes for inspiration!"
    }

@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}

@app.get("/business_ideas")
def get_business_ideas():
    """Returns a random business idea"""
    return {"business_idea": random.choice(business_ideas)}

@app.get("/motivational_quotes")
def get_motivational_quotes():
    """Returns a random motivational quote"""
    return {"motivational_quote": random.choice(motivational_quotes)}


