import random


def get_html(receiver, sender, category, index=0):

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
        <div
            style="display: flex; flex-direction: row;width: 90%;height: 8rem; margin: 2.5%; background-color: rgb(243, 243, 243); padding: 10px;border-radius: 20px;">
            <div style="flex: 1; height: fit-content; position: relative; top: 1rem;  left: 10px;">
                <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                    style="width: 6rem; height: 6rem; border-radius: 10px;">
            </div>
            <div
                style=" padding-left: 20px; flex: 5; display: flex; flex-direction: column; justify-content:center; margin-top: -20px;">
                <div
                    style=" color: #121212;text-shadow: 0.5px 0.5px 0.5px #000; font-weight: 1000; font-size: 1.25rem;">
                    Cher8: Web3 Life br /ochure Social Platform</div>
                <div style="color: gray; text-indent: 1px; font-size: 1rem;"> Your life guide platform</div>
            </div>
        </div>
    </a>
    <h3 style="color: gray;">Dear {receiver},</h3>
    <p style="font-size: 18px; font-weight: 600; color: gray;">
        This is {sender} and I represent Cher8, a pioneering web3 social platform focused on lifeguides and lifestyle
        <br />
        <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8:</strong>
    <br />
    <br />
    Cher8 is a blockchain-powered social community platform that values
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">freedom of speech, privacy security,</strong>
    and <strong style="color: #121212; font-size: 20px; font-weight: 800;">fair rewards</strong>. We believe that these values align perfectly with your own principles and
    creative style.
    <br />
    <br />
    
<a href="https://www.cher8.com/invite-link?key=influencer">
    <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/image1.png"
        style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
</a>
    <br />
    <br />
    After researching your work and creative style, we are confident that your talents in sharing content on {category}
    can be amplified on our platform.
    <br />
    <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Proposals:</strong>
    <br />
    <br />
    To demonstrate our sincerity and commitment to working with you, I have attached our collaboration proposals for
    your review.
    <br />
    <br />
    Please also check out the possible plan below and click to get more details.
    <a href="https://www.cher8.com/invite-link?key=influencer">
        <img src=" https://cher8-app.s3.us-east-2.amazonaws.com/ops/image2.png"
            style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
    </a>
    <br />
    <br />
    Does this sound interesting? If so, I would really love to get in touch and begin a collaboration that would bring
    values to both our audience.
    <br />
    <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8 Info:</strong>
    <br />
    <br />
    Our official website: <a href="https://www.cher8.com">www.cher8.com</a>
    <br />
    App Store/Google Play Download: <a href="https://www.cher8.com/invite-link?key=download">
        www.cher8.com/invite-link?key=download</a>
    <br />
    <br />
    Best Regards,
    <br />
    <br />
    {sender}
    </p>
    <div>
        <div style="margin-top: 10px; text-align: center; color: gray; font-size: 14px;">For help with plans and
            technical support,email at support@cher8.com</div>

        <div style=" text-align: center; "><img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                style="width: 50px; height: 50px;"> </div>
        <div style="text-align: center; color: gray; font-size: 12px;">Copyright © 2023 Cher8 Inc</div>
    </div>
</body>

</html>
"""


    html_text_2 = f"""
  <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cher8-invitation</title>
</head>

<body>
    <a href="#" style="text-decoration: none;">
        <div
            style="display: flex; flex-direction: row;width: 90%;height: 8rem; margin: 2.5%; background-color: rgb(243, 243, 243); padding: 10px;border-radius: 20px;">
            <div style="flex: 1; height: fit-content; position: relative; top: 1rem;  left: 10px;">
                <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                    style="width: 6rem; height: 6rem; border-radius: 10px;">
            </div>
            <div
                style=" padding-left: 20px; flex: 5; display: flex; flex-direction: column; justify-content:center; margin-top: -20px;">
                <div
                    style=" color: #121212;text-shadow: 0.5px 0.5px 0.5px #000; font-weight: 1000; font-size: 1.25rem;">
                    Cher8: Web3 Life br /ochure Social Platform</div>
                <div style="color: gray; text-indent: 1px; font-size: 1rem;"> Your life guide platform</div>
            </div>
        </div>
    </a>
    <h3 style="color: gray;">Dear {receiver},</h3>
    <p style="font-size: 18px; font-weight: 600; color: gray;">
        This is {sender} and I represent Cher8, a pioneering web3 social platform focused on life guides and lifestyle
        <br />
        <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8:</strong>
    <br />
    <br />
    Cher8 is a blockchain-powered social community platform that values
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">freedom of speech, privacy security,</strong>
    and <strong style="color: #121212; font-size: 20px; font-weight: 800;">fair rewards</strong>. We believe that these values align perfectly with your own principles and
    creative style.
    <br />
    <br />
    
<a href="https://www.cher8.com/invite-link?key=influencer">
    <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/image1.png"
        style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
</a>
    <br />
    <br />
    After researching your work and creative style, we are confident that your talents in sharing content on {category}
    can be amplified on our platform.
    <br />
    <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Proposals:</strong>
    <br />
    <br />
    To demonstrate our sincerity and commitment to working with you, I have attached our collaboration proposals for
    your review.
    <br />
    <br />
    Please also check out the possible plan below and click to get more details.
    <a href="https://www.cher8.com/invite-link?key=influencer">
        <img src=" https://cher8-app.s3.us-east-2.amazonaws.com/ops/ops_email_2.png"
            style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
    </a>
    <br />
    <br />
    Does this sound interesting? If so, I would really love to get in touch and begin a collaboration that would bring
    values to both our audience.
    <br />
    <br />
    <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8 Info:</strong>
    <br />
    <br />
    Our official website: <a href="https://www.cher8.com">www.cher8.com</a>
    <br />
    App Store/Google Play Download: <a href="https://www.cher8.com/invite-link?key=download">
        www.cher8.com/invite-link?key=download</a>
    <br />
    <br />
    Best Regards,
    <br />
    <br />
    {sender}
    </p>
    <div>
        <div style="margin-top: 10px; text-align: center; color: gray; font-size: 14px;">For help with plans and
            technical support,email at support@cher8.com</div>

        <div style=" text-align: center; "><img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                style="width: 50px; height: 50px;"> </div>
        <div style="text-align: center; color: gray; font-size: 12px;">Copyright © 2023 Cher8 Inc</div>
    </div>
</body>

</html>
    """

    html_text_3 = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cher8-invitation</title>
</head>

<body>
    <a href="#" style="text-decoration: none;">
        <div
            style="display: flex; flex-direction: row;width: 90%;height: 8rem; margin: 2.5%; background-color: rgb(243, 243, 243); padding: 10px;border-radius: 20px;">
            <div style="flex: 1; height: fit-content; position: relative; top: 1rem;  left: 10px;">
                <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                    style="width: 6rem; height: 6rem; border-radius: 10px;">
            </div>
            <div
                style=" padding-left: 20px; flex: 5; display: flex; flex-direction: column; justify-content:center; margin-top: -20px;">
                <div
                    style=" color: #121212;text-shadow: 0.5px 0.5px 0.5px #000; font-weight: 1000; font-size: 1.25rem;">
                    Cher8: Web3 Life br /ochure Social Platform</div>
                <div style="color: gray; text-indent: 1px; font-size: 1rem;"> Your life guide platform</div>
            </div>
        </div>
    </a>
    <h3 style="color: gray;">Dear {receiver},</h3>
    <p style="font-size: 18px; font-weight: 600; color: gray;">
        I love your photograph.
        <br />
        <br />
        This is {sender} and I represent Cher8, a pioneering web3 social platform focused on lifeguides and lifestyle.
        <br />
        <br />
        <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8:</strong>
        <br />
        <br />
        Cher8 is a blockchain-powered social community platform that values
        <strong style="color: #121212; font-size: 20px; font-weight: 800;">freedom of speech, privacy security,
        </strong>
        and <strong style="color: #121212; font-size: 20px; font-weight: 800;">fair rewards</strong>. We believe that
        these values <strong style="color: #121212; font-size: 20px; font-weight: 800;">align perfectly</strong> with
        your own principles and creative style.
        <br />
        <br />
        <a href="https://www.cher8.com/invite-link?key=influencer">
            <img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/image1.png"
                style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
        </a>
        <br />
        <br />
        After researching your work and creative style, we are confident that your talents in sharing content on
        {category} can be amplified on our platform.
        <br />
        <br />
        <strong style="color: #121212; font-size: 20px; font-weight: 800;">Proposals:</strong>
        <br />
        <br />
        To demonstrate our sincerity and commitment to working with you, I have attached our collaboration proposals for
        your review.
        <br />
        <br />
        Please also check out the possible plan below and click to get more details.
        <a href="https://www.cher8.com/invite-link?key=influencer">
            <img src=" https://cher8-app.s3.us-east-2.amazonaws.com/ops/ops_email_2.png"
                style="width: 95%; margin: 2.5%; aspect-ratio: 2;" alt="">
        </a>
        <br />
        <br />
        Does this sound interesting? If so, I would really love to get in touch and begin a collaboration that would
        bring values to both our audience.
        <br />
        <br />
        <strong style="color: #121212; font-size: 20px; font-weight: 800;">Cher8 Info:</strong>
        <br />
        <br />
        Our official website: <a href="https://www.cher8.com">www.cher8.com</a>
        <br />
        App Store/Google Play Download: <a href="https://www.cher8.com/invite-link?key=download">
            www.cher8.com/invite-link?key=download</a>
        <br />
        <br />
        Best Regards,
        <br />
        <br />
        {sender}
    </p>
    <div>
        <div style="margin-top: 10px; text-align: center; color: gray; font-size: 14px;">For help with plans and
            technical support,email at support@cher8.com</div>

        <div style=" text-align: center; "><img src="https://cher8-app.s3.us-east-2.amazonaws.com/ops/icon.png" alt=""
                style="width: 50px; height: 50px;"> </div>
        <div style="text-align: center; color: gray; font-size: 12px;">Copyright © 2023 Cher8 Inc</div>
    </div>
</body>

</html>
    """

    html_template_list = [html_text_1, html_text_2, html_text_3]

    if index == 0:
        return random.choice(html_template_list)
    else:
        return html_template_list[index - 1]
