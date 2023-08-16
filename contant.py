import random


def get_html(receiver, index=0):
    html_text_1 = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cher8-invitation</title>
</head>

<body>
    <a href="#" style="text-decoration: none;">
        <div style="display: flex; flex-direction: row;width: 90%;height: 8rem; margin: 2.5%; background-color: rgb(243, 243, 243); padding: 10px;border-radius: 20px;">
            <div style="flex: 1; height: fit-content; position: relative; top: 1rem;  left: 10px;">
                <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt="" style="width: 6rem; height: 6rem; border-radius: 10px;">
            </div>
            <div style=" padding-left: 20px; flex: 5; display: flex; flex-direction: column; justify-content:center; margin-top: -20px;">
                <div style=" color: #121212;text-shadow: 0.5px 0.5px 0.5px #000; font-weight: 1000; font-size: 1.25rem;">Cher8-life brochure: Share, Earn,Fair</div>
                <div style="color: gray; text-indent: 1px; font-size: 1rem;">Transform your unique creations into valuable rewards and embrace a fair and
                    transparent ecosystem</div>
            </div>
        </div>
    </a>
    <a  href="https://www.cher8.com/invite-link?key=influencer">
      <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/ops_email_1.png"
        style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
    </a>
    <h3 style="color: gray;">Dear {receiver},</h3>
    <p style="font-size: 18px; font-weight: 600; color: gray;">
        Congratulations on being selected to join our exclusive creator program,
        where we guarantee that your creations will be transformed into rewards.
        <br>
        <br>
        Have you ever imagined a web3+AI version of Pinterest? Well, Cher8 is
        better than that! 
        <br>
        <br>
        At Cher8, we are committed to fostering a vibrant and unprecedented
        community of creators, ensuring that your talents are acknowledged and
        compensated.
        <br>
        <br>
        Our mission at Cher8 is to provide users with insightful and engaging
        content that caters to their situational and entertainment needs. We believe
        in treating every creator fairly, regardless of the size of their following. With
        Cher8, you will be compensated for your creations based on even a single
        interaction, such as a like, collection, or comment.
        <br>
        <br>
        Still curious to know more? Join us now
    </p>
    
    <a href="https://www.cher8.com/invite-link?key=influencer">
        <img src=" https://cher8-app.s3.us-east-2.amazonaws.com/ops/ops_email_2.png"
          style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
      </a>
      <hr>
      <p style="font-size: 18px; font-weight: 600; color: gray;">
        In addition to rewarding your efforts, Cher8 has partnered with numerous
        brands, opening up exciting collaboration opportunities for you. We are
        thrilled to empower you with these valuable connections.
        <br>
        <br>
        We understand the frustration of unpaid creations and the desire to
        showcase your professional skills. Cher8 is the ultimate platform for you,
        designed to streamline your creative journey and provide quicker and easier
        access to your desired audience.
        <br>
        <br>
        Join now and start revolutionizing the way you create on Cher8.
        <br>
        <br>
        Download Now：<a href="https://www.cher8.com/invite-link?key=download">www.cher8.com/invite-link?key=download</a>
        <br>
        <br>
        Best regards,
        <br>
        Cher8 Creator Center
    </p>
    <div>
        <div style="margin-top: 10px; text-align: center; "><img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt="" style="width: 50px; height: 50px;"> </div>
        <div style="text-align: center; color: gray; font-size: 12px;">Copyright © 2023 Cher8 Inc</div>
    </div>
</body>

</html>  """


    html_template_list = [html_text_1]

    if index == 0:
        return random.choice(html_template_list)
    else:
        return html_template_list[index-1]