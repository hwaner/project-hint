package kr.hwaner.spring.hint.user;

import lombok.AllArgsConstructor;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

import java.util.Random;

/**
 * @author hwaner
 */
@Service
@AllArgsConstructor
public class MailServiceImpl implements MailService {

    private JavaMailSender mailSender;
    private static final String FROM_ADDRESS = "hanahintmanager@gmail.com";

    @Override
    public void mailSend(User user) {

        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(user.getEmailId());
        message.setFrom(FROM_ADDRESS);
        message.setSubject("[HINT] 의 임시 비밀번호가 발급되었습니다.");
        message.setText(String.format("안녕하세요, HINT 입니다. 임시로 발급된 비밀번호는 '%s'입니다. " +
                "로그인 후 반드시 비밀번호를 변경해주시길 바랍니다.", user.getPassword()));
        mailSender.send(message);
    }

    @Override
    public String init() {

        Random random = new Random(System.currentTimeMillis());
        StringBuffer buf = new StringBuffer();

        char[] characterTable = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };
        int certCharLength = 8;
        int length = characterTable.length;
        for(int i = 0; i < certCharLength; i++ ){

            buf.append(characterTable[random.nextInt(length)]);
        }

        return buf.toString();
    }
}
