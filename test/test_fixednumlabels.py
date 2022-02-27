from torch_multilabel_embedding import MultiLabelEmbedding
import torch


def test1():
    # the lookup based Embedding
    examples = [[1, 2, 4], [0, 1, 2], [2, 1, 4], [3, 2, 1]]
    examples = torch.tensor(examples)
    layer1 = MultiLabelEmbedding(
        vocab_size=5, embed_size=300, random_state=42)
    y1 = layer1(examples)
    # the linear layer
    examples = [[0., 1, 1, 0, 1], [1, 1, 1, 0, 0],
                [0, 1, 1, 0, 1], [0, 1, 1, 1, 0]]
    examples = torch.tensor(examples)
    layer2 = torch.nn.Linear(5, 300, bias=False)
    layer2.weight = torch.nn.parameter.Parameter(layer1.weight.detach().T)
    y2 = layer2(examples)
    # compare
    torch.testing.assert_close(y1, y2)
